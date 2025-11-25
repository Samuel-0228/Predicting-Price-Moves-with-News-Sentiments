import pandas as pd


class NewsFeatureExtractor:
    def __init__(self, df):
        self.df = df

    def headline_length(self):
        """Add length feature."""
        self.df['headline_length'] = self.df['title'].str.len()
        return self.df

    def publisher_counts(self):
        """Value counts."""
        return self.df['publisher'].value_counts().head(10)
