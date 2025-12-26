import streamlit as st


def upload_market_data():
    st.subheader("📥 Upload Market Data")
    st.caption(
        "Upload historical market price data (CSV format). "
        "The file must contain a 'Close' price column."
    )

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    return file


def display_metrics(vol_forecast):
    st.subheader("📊 Risk Forecast")
    st.metric(label="Predicted Next-Period Volatility", value=f"{vol_forecast:.4f}")

    # --- Dynamic explanation ---
    if vol_forecast > 0.05:
        st.warning("High predicted volatility → market uncertainty increasing, higher risk.")
    else:
        st.success("Low predicted volatility → market is relatively stable, lower risk.")

