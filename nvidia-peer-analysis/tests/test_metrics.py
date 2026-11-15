import numpy as np
import pytest

from src.metrics import annualized_sharpe


def test_annualized_sharpe_for_known_returns():
    excess_returns = np.array([0.00, 0.01, 0.02])

    result = annualized_sharpe(excess_returns)

    assert result == pytest.approx(15.874508)
