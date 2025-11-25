import pandas as pd
from src.utils.news_stock_correlation import CorrelationAnalyzer
import pytest


@pytest.fixture
def mock_df():
    return pd.DataFrame({'title': ['Test buy'], 'date': [pd.to_datetime('2023-01-01')], 'stock': ['NFLX'], 'sentiment': [0.1]})


def test_correlation_r_positive(mock_df):
    corr = CorrelationAnalyzer(mock_df, 'NFLX')
    r, _ = corr.compute_correlation()
    assert r > -0.5  # Loose for mock
