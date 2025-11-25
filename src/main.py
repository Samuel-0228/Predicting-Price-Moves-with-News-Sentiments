import pandas as pd
from src.utils.data_loading import DataLoader
from src.utils.sentiment import SentimentAnalyzer
from src.utils.news_stock_correlation import CorrelationAnalyzer
from src.utils.technical_indicators import TechnicalAnalyzer

if __name__ == "__main__":
    # Load data
    loader = DataLoader('data/raw_analyst_ratings.csv')
    df = loader.load_sample(n=50000)

    # Sentiment
    analyzer = SentimentAnalyzer()
    df['sentiment'] = df['title'].apply(analyzer.analyze)
    print(f"Avg Sentiment: {df['sentiment'].mean():.3f}")

    # Quick corr (top stock)
    corr = CorrelationAnalyzer(df, 'NFLX')
    r, p = corr.compute_correlation()
    print(f"NFLX r: {r:.3f}, p: {p:.3f}")

    # Indicators
    tech = TechnicalAnalyzer('NFLX')
    rsi = tech.rsi()
    print(f"NFLX RSI mean: {rsi.mean():.3f}")
