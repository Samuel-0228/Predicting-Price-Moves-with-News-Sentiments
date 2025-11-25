import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_sample(self, n=50000):
        """Load and sample data."""
        df = pd.read_csv(self.file_path, low_memory=False)
        df['date'] = pd.to_datetime(df['date'])
        return df.sample(n=n, random_state=42) if len(df) > n else df
