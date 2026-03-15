"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_function import clean_column, compute_revenue


def test_clean_column():
        
    # TODO: Create a pd.Series with at least one NaN value
        test_series = pd.Series([10, 20, np.nan, 40, 50])

    # TODO: Call clean_column() on it
        result = clean_column(test_series)

    # TODO: Assert no NaN values remain in the result
        assert result.isna().sum() == 0

    # TODO: Assert the NaN was filled with the correct median value
        assert result[2] == 30.0


def test_compute_revenue():

    # TODO: Create two small pd.Series (quantity and price)
    qty = pd.Series([2, 5, 1])
    price = pd.Series([10.0, 20.0, 100.0])

    # TODO: Call compute_revenue() on them
    result = compute_revenue(qty, price)

    # TODO: Assert the result matches the expected element-wise product
    expected = pd.Series([20.0, 100.0, 100.0])
    pd.testing.assert_series_equal(result, expected)

