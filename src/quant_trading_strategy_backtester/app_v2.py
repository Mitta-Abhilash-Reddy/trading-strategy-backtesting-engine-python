import streamlit as st
import datetime
import polars as pl

from quant_trading_strategy_backtester.data import (
    load_yfinance_data_one_ticker,
    load_yfinance_data_two_tickers,
)
from quant_trading_strategy_backtester.backtester import Backtester
from quant_trading_strategy_backtester.strategies.moving_average_crossover import MovingAverageCrossoverStrategy
from quant_trading_strategy_backtester.strategies.rsi_strategy import RSIStrategy
from quant_trading_strategy_backtester.visualisation import plot_equity_curve, plot_strategy_returns
from quant_trading_strategy_backtester.optimiser import run_backtest

# --------------------------- UI CONFIG ---------------------------

st.set_page_config(
    page_title="Quant Trading Backtester",
    layout="wide",
    page_icon="📈"
)

st.title("📈 Quant Trading Strategy Backtester — Modern Dashboard")

# Sidebar Navigation
page = st.sidebar.radio(
    "Navigation",
    ["Run Backtest", "Optimisation", "Historical Results", "About"],
    index=0
)

# --------------------------- RUN BACKTEST PAGE ---------------------------

if page == "Run Backtest":
    st.header("Run a Backtest")

    col1, col2 = st.columns(2)

    with col1:
        ticker = st.text_input("Ticker (e.g., AAPL, MSFT)", "AAPL")
        start_date = st.date_input("Start Date", datetime.date(2020, 1, 1))
        end_date = st.date_input("End Date", datetime.date(2023, 12, 31))

    with col2:
        strategy_name = st.selectbox(
            "Select Strategy",
            ["Moving Average Crossover", "RSI Strategy"]
        )

        if strategy_name == "Moving Average Crossover":
            short = st.number_input("Short Window", 5, 50, 20)
            long = st.number_input("Long Window", 20, 200, 50)
            params = {"short_window": short, "long_window": long}

        elif strategy_name == "RSI Strategy":
            window = st.number_input("RSI Window", 5, 50, 14)
            lower = st.number_input("Oversold Level", 10, 40, 30)
            upper = st.number_input("Overbought Level", 60, 90, 70)
            params = {"window": window, "lower": lower, "upper": upper}

    run_button = st.button("Run Backtest 🚀")

    if run_button:
        st.info("Fetching Data...")
        data = load_yfinance_data_one_ticker(ticker, start_date, end_date)

        # Choose strategy
        if strategy_name == "Moving Average Crossover":
            strategy = MovingAverageCrossoverStrategy(params)
        else:
            strategy = RSIStrategy(params)

        st.info("Running Backtest...")
        bt = Backtester(data, strategy)
        results = bt.run()
        metrics = bt.get_performance_metrics()

        st.success("Backtest Complete 🎉")

        # Metric Cards
        st.subheader("Performance Summary")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Return", f"{metrics['Total Return']:.2%}")
        m2.metric("Sharpe Ratio", f"{metrics['Sharpe Ratio']:.2f}")
        m3.metric("Max Drawdown", f"{metrics['Max Drawdown']:.2%}")
        m4.metric("CAGR", f"{metrics['CAGR']:.2%}")

        st.subheader("Equity Curve")
        import os
        image_path = r"C:\Users\hi\Desktop\projects\QUANT\quant-trading-strategy-backtester\equity_curve.png"
        st.image(image_path)



        st.subheader("Strategy Returns by Month")
        plot_strategy_returns(results, ticker, ticker)

# --------------------------- ABOUT SECTION ---------------------------

elif page == "About":
    st.write("### 💡 About This Project")
    st.write("""
    This is a modern quantitative backtesting platform built using:
    - **Polars**
    - **Streamlit**
    - **SQLAlchemy**
    - **Plotly**
    - **yfinance**

    Features:
    - Multiple strategies (MA Crossover, RSI, Mean Reversion, Pairs Trading)
    - Optimisation engine
    - Full performance metrics (Sharpe, Sortino, Profit Factor)
    - Interactive visual dashboards
    """)
