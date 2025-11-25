import yfinance as yf
import talib


class TechnicalAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker, start='2015-01-01')['Close']

    def rsi(self, period=14):
        """RSI via TA-Lib."""
        return talib.RSI(self.data, timeperiod=period)

    def sma(self, period=20):
        """SMA."""
        return talib.SMA(self.data, timeperiod=period)
