# AI Market Risk Analyser 📈🤖

## Live Application
https://pricingengine-ck2yv7wpokb8wdmr4owzhd.streamlit.app/

## Project Overview
AI Market Risk Analyser is an end-to-end AI-powered financial analytics system that combines traditional options pricing models with machine learning–based forecasting. The application provides option pricing, Greeks computation, AI-driven option price prediction, and volatility forecasting through an interactive Streamlit interface.

## Key Features

### Option Pricing
- Computes option prices using financial parameters
- Supports real-time parameter input
- Designed for quick quantitative analysis

### Greeks Calculation
- Delta
- Gamma
- Vega
- Theta
- Rho
- Helps in understanding market risk sensitivity

### AI Price Prediction
- Machine Learning–based option price prediction
- Feature engineering with moneyness and time-based features
- Random Forest Regressor used for prediction
- Pre-trained model and preprocessor loaded for cloud deployment

### AI Volatility Forecasting
- Predicts future volatility using historical returns
- Uses returns and squared returns as features
- Ridge Regression model for stability and regularization

## Machine Learning Pipeline

### Price Prediction Model
- Algorithm: Random Forest Regressor
- Preprocessing:
  - Feature engineering
  - Standard scaling
- Saved Models:
  - price_model.pkl
  - price_preprocessor.pkl

### Volatility Prediction Model
- Algorithm: Ridge Regression
- Features:
  - Returns
  - Returns squared
- Saved Model:
  - vol_model.pkl

## Project Structure
options-pricing-engine/
│
├── ai/
│ ├── price_model.py
│ ├── volatility_model.py
│ ├── preprocessing.py
│ ├── trainer.py
│ └── model_store/
│ ├── price_model.pkl
│ ├── price_preprocessor.pkl
│ └── vol_model.pkl
│
├── data/
│ └── options_data.csv
│
├── streamlit_app/
│ └── sections/
│ ├── pricing_section.py
│ ├── greeks_section.py
│ ├── ai_price_section.py
│ └── ai_vol_section.py
│
├── app.py
├── requirements.txt
└── README.md

## Deployment
- Deployed on Streamlit Cloud
- Models are pre-trained and committed for cloud execution
- No runtime training required

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Git and GitHub

## Use Cases
- Market risk analysis
- Options pricing experimentation
- Volatility forecasting
- Financial machine learning portfolio project

## Author
Yashaswi Bisht  
B.Tech | Machine Learning and Artificial Intelligence

## Future Enhancements
- Deep learning models for volatility forecasting
- Real-time market data integration
- Monte Carlo simulation support
- Advanced risk dashboards
