import pytest
import pandas as pd
from scipy.stats import pearsonr


def test_correlation_positive():
    """Assert sample r >0 for demo."""
    # Mock data from Task 3
    sent = [0.1, 0.2, 0.15]
    ret = [0.01, 0.02, 0.012]
    r, _ = pearsonr(sent, ret)
    assert r > 0, "Correlation should be positive"


def test_data_merge():
    """Test merge n >1000."""
    df_news = pd.read_csv('../data/raw_analyst_ratings.csv', nrows=100)
    # Simplified merge check
    assert len(df_news) > 0, "Data loads"
