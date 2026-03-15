import pandas as pd

def clean_column(series):
    """Fill NaN values with the series median. Returns the cleaned Series."""

    cleaned_series = series.fillna(series.median())
    return cleaned_series

# To Fill NaN values  == .fillna
# To calculate the median == .median

def compute_revenue(quantity, price):
    """Multiply quantity and price element-wise. Returns a revenue Series."""

    revenue = quantity * price
    return revenue

# cuantity: [2, 5, 1]
# price: [10, 20, 100]
# revenue = quantity * price
# revenue: [20, 100, 100]
