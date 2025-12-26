import numpy as np
import joblib
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


MODEL_PATH = "models/risk_model.pkl"


def train_risk_model(df):
    """
    Train a Ridge Regression model to forecast volatility
    """

    features = ["volatility_lag1", "returns_lag1"]
    target = "volatility"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # Save model
    joblib.dump(model, MODEL_PATH)

    return mse


def predict_risk(model, last_vol, last_return):
    """
    Predict next-period volatility
    """

    X = np.array([[last_vol, last_return]])
    forecast = model.predict(X)[0]

    return forecast
