import streamlit as st
import joblib
import os

from core.data_processing import load_market_data, compute_features
from core.risk_forecasting import train_risk_model, predict_risk
from core.regime_detection import train_regime_model, detect_regimes
from core.anomaly_detection import train_anomaly_model, detect_anomalies

from app.ui import upload_market_data, display_metrics
from app.plots import plot_price_series, plot_regimes, plot_anomalies


def run_app():
    st.title("📊 AI-Driven Market Risk Monitoring System")

    file = upload_market_data()

    if file is not None:
        # --- Load & preprocess data ---
        df = load_market_data(file)
        df = compute_features(df)

        # --- Train OR Load Models (PERFORMANCE FIX) ---
        if not os.path.exists("models/risk_model.pkl"):
            train_risk_model(df)

        risk_model = joblib.load("models/risk_model.pkl")

        if not os.path.exists("models/regime_model.pkl"):
            regime_model = train_regime_model(df)
        else:
            regime_model = joblib.load("models/regime_model.pkl")

        if not os.path.exists("models/anomaly_model.pkl"):
            anomaly_model = train_anomaly_model(df)
        else:
            anomaly_model = joblib.load("models/anomaly_model.pkl")

        # --- Forecast Risk ---
        last_vol = df["volatility"].iloc[-1]
        last_return = df["returns"].iloc[-1]

        forecast = predict_risk(
            risk_model,
            last_vol,
            last_return
        )

        # --- Regime & Anomaly Detection ---
        df["regime"] = detect_regimes(regime_model, df)
        df["anomaly"] = detect_anomalies(anomaly_model, df)

        # --- UI Output ---
        display_metrics(forecast)
        plot_price_series(df)
        plot_regimes(df)
        plot_anomalies(df)
