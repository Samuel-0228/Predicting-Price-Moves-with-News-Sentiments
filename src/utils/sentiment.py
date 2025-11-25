from textblob import TextBlob


class SentimentAnalyzer:
    def analyze(self, text):
        """Compute polarity."""
        return TextBlob(str(text)).sentiment.polarity

    def batch_analyze(self, series):
        """Vectorized for df."""
        return series.apply(self.analyze)
