import numpy as np


def annualized_sharpe(excess_returns, trading_days_per_year=252):
    """Calculate the annualized Sharpe ratio from daily excess returns."""
    mean_return = excess_returns.mean(axis=0)
    volatility = excess_returns.std(axis=0, ddof=1)
    return mean_return / volatility * np.sqrt(trading_days_per_year)
