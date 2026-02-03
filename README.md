# 📈 Trader Behavioral Analysis: Fear vs. Greed

## 📝 Project Overview

This project analyzes trader performance and behavioral archetypes in response to market sentiment (Fear & Greed Index). By merging high-frequency trade data with sentiment indicators, we identify how different trader segments adapt their risk management and position sizing during various market cycles.

## 🚀 Key Features

- **Data Pipeline:** Automated cleaning and alignment of UTC/IST timestamps across datasets.
- **Behavioral Clustering:** Used K-Means clustering to identify three distinct archetypes: _High-Frequency Scalpers_, _Permabull Trend Followers_, and _Calculated Contrarians_.
- **Predictive Modeling:** A Random Forest classifier to determine the impact of sentiment on trade profitability.
- **Actionable Insights:** Two data-driven "Rules of Thumb" for risk mitigation during extreme sentiment shifts.

## 📊 Core Findings

1. **The Size Bias:** Our Feature Importance analysis revealed that `Size USD` is the dominant predictor of PnL, suggesting a potential lack of sentiment-based adjustment among retail traders.
2. **Sentiment Sensitivity:** Scalpers show significantly higher PnL volatility during "Fear" days compared to "Greed" days.
3. **Archetype Divergence:** Trend followers tend to increase leverage during "Greed" peaks, leading to higher drawdown risks.

## 🛠️ Installation & Usage

1. **Create Virtual Environment:**
   ```bash
   python -m venv sentiment_analysis
   source sentiment_analysis/bin/activate  # Or .\sentiment_analysis\Scripts\activate on Windows
   ```

   
## 🖥️ How to Run the Interactive Dashboard
I have included a Streamlit dashboard to visualize the behavioral clusters and sentiment analysis interactively.

1. **Activate the environment:**
   ```powershell
   .\sentiment_analysis\Scripts\Activate.ps1
