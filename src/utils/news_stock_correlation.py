import yfinance as yf
from scipy.stats import pearsonr
import pandas as pd


class CorrelationAnalyzer:
    def __init__(self, df_news, stock):
        self.df_news = df_news
        self.stock = stock
        self.df_stock = yf.download(stock, start='2015-01-01')['Adj Close']
        self.df_stock = pd.DataFrame(self.df_stock).reset_index()
        self.df_stock['date'] = pd.to_datetime(self.df_stock['Date']).dt.date
        self.df_stock['returns'] = self.df_stock['Adj Close'].pct_change(
        ).shift(-1)

    def aggregate_sentiment(self):
        """Daily mean sent per stock."""
        daily_sent = self.df_news[self.df_news['stock'] == self.stock].groupby('date')[
            'sentiment'].mean().reset_index()
        daily_sent['date'] = pd.to_datetime(daily_sent['date']).dt.date
        return daily_sent

    def compute_correlation(self):
        """Pearson r sent vs returns."""
        daily_sent = self.aggregate_sentiment()
        merged = self.df_stock.merge(daily_sent, on='date', how='left')
        merged['sentiment'].fillna(0, inplace=True)
        mask = merged.dropna()
        r, p = pearsonr(mask['sentiment'], mask['returns'])
        return r, p
