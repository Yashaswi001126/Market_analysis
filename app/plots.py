import matplotlib.pyplot as plt
import streamlit as st


def plot_price_series(df):
    st.subheader("📈 Price Series")

    fig, ax = plt.subplots()
    ax.plot(df["Close"])
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    st.pyplot(fig)

    # --- Dynamic explanation ---
    if df["Close"].iloc[-1] > df["Close"].iloc[0]:
        st.info("The price has generally increased → bullish trend, potential opportunity but watch for volatility.")
    elif df["Close"].iloc[-1] < df["Close"].iloc[0]:
        st.warning("The price has generally decreased → bearish trend, potential downside risk.")
    else:
        st.write("The price is roughly stable → neutral trend, lower directional risk.")



def plot_regimes(df):
    st.subheader("🧠 Market Regimes")

    fig, ax = plt.subplots()
    scatter = ax.scatter(
        df.index,
        df["Close"],
        c=df["regime"],
        cmap="viridis"
    )
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    st.pyplot(fig)

    # --- Explain regimes ---
    regime_counts = df["regime"].value_counts()
    st.write("Market regime breakdown:")
    for r, count in regime_counts.items():
        st.write(f"Regime {r}: {count} days")
    st.info("Regimes indicate market risk environment: higher-numbered regimes → higher volatility / risk.")



def plot_anomalies(df):
    st.subheader("🚨 Anomaly Detection")

    fig, ax = plt.subplots()
    ax.plot(df["Close"], label="Price")

    anomalies = df[df["anomaly"] == -1]
    ax.scatter(
        anomalies.index,
        anomalies["Close"],
        color="red",
        label="Anomaly"
    )

    ax.legend()
    st.pyplot(fig)

    # --- Dynamic explanation ---
    if len(anomalies) > 0:
        st.warning(f"Detected {len(anomalies)} anomalies → unusual market movements, potential tail risk.")
    else:
        st.success("No anomalies detected → market movements are normal.")

