import numpy as np
import pandas as pd
import pytest

from src.metrics import annualized_sharpe


def test_annualized_sharpe_for_known_returns():
    excess_returns = np.array([0.00, 0.01, 0.02])

    result = annualized_sharpe(excess_returns)

    assert result == pytest.approx(15.874508)

def test_annualized_sharpe_by_stock():
    excess_returns = pd.DataFrame({
        "Stock A": [0.00, 0.01, 0.02],
        "Stock B": [-0.01, 0.00, 0.01],
    })

    result = annualized_sharpe(excess_returns)

    assert list(result.index) == ["Stock A", "Stock B"]
    assert result["Stock A"] == pytest.approx(15.874508)
    assert result["Stock B"] == pytest.approx(0.0)
