import scipy.stats as stats
import pandas as pd


class StatsMetrics:
    @staticmethod
    def descriptive(series):
        """Basic stats."""
        return series.describe()

    @staticmethod
    def pearson_r(x, y):
        """Custom r with p."""
        return pearsonr(x, y)

    @staticmethod
    def distribution_fit(series, dist='norm'):
        """Fit test (e.g., lognorm)."""
        if dist == 'lognorm':
            return stats.log.norm.fit(series)
