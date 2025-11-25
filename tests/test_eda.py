import pytest
import pandas as pd
import os


def test_placeholder():
    assert True


def test_data_load():
    """Skips automatically in CI if data not available."""
    file_path = os.path.join("data", "raw_analyst_ratings.csv")

    if not os.path.exists(file_path):
        pytest.skip("Data not found in CI environment")

    df = pd.read_csv(file_path, nrows=10)
    assert not df.empty
