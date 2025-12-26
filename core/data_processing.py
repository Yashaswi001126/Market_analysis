import pandas as pd
import numpy as np


def load_market_data(file):
    """
    Load CSV file and validate required columns
    """
    df = pd.read_csv(file)

    if "Close" not in df.columns:
        raise ValueError("CSV must contain a 'Close' column")

    df = df.dropna()
    return df


def compute_features(df, window=20):
    """
    Feature engineering for market risk
    """

    # Daily returns
    df["returns"] = df["Close"].pct_change()

    # Rolling volatility
    df["volatility"] = df["returns"].rolling(window).std()

    # Lagged volatility
    df["volatility_lag1"] = df["volatility"].shift(1)

    # Lagged returns
    df["returns_lag1"] = df["returns"].shift(1)

    df = df.dropna()

    return df
