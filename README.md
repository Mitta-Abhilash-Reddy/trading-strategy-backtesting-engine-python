# Quant Trading Strategy Backtester

A modular Python-based quantitative trading backtesting engine with multiple strategies, parameter optimisation, rich performance analytics, and an interactive Streamlit dashboard.[1]

***

## Overview

This project provides an end-to-end workflow for researching and validating systematic trading strategies using historical market data.  It is suitable for learning algorithmic trading concepts, rapid strategy iteration, and showcasing as a resume-ready quant/fintech project.[2][1]

***

## Features

- Fetches historical OHLCV data using `yfinance` for any supported ticker.[3]
- Runs predefined or custom strategies through a modular backtesting engine.[1]
- Computes portfolio returns, PnL, drawdowns, and institutional-grade metrics (Sharpe, Sortino, CAGR, max drawdown).[4]
- Supports parameter optimisation and automatic selection of best-performing tickers.[1]
- Persists runs to SQLite via SQLAlchemy for historical comparison and reproducibility.[1]
- Visualises results and comparisons through an interactive Streamlit dashboard.[5][6]

***

## Tech Stack

- **Language**: Python 3.8+  
- **Data Engine**: Polars, Pandas  
- **Market Data**: `yfinance`  
- **UI Dashboard**: Streamlit  
- **Database**: SQLite + SQLAlchemy  
- **Testing**: pytest  
- **Visualisation**: Matplotlib / Plotly[7][1]

***

## Backtesting Engine

- Vectorised return computation using Polars for fast backtests on large datasets.[3]
- Supports long/flat and long/short position signals with equity curve tracking.[4]
- Tracks cumulative returns, daily returns, trade count, win rate, profit factor, and risk-adjusted metrics.[8]

***

## Included Strategies

- Moving Average Crossover  
- RSI-based Trading Strategy  
- Mean Reversion Strategy  
- (Optional extension) Pairs Trading framework[9][1]

Each strategy inherits from a common base class, making it easy to plug in custom logic or extend existing strategies.[3]

***

## Analytics & Metrics

The engine computes commonly used performance statistics for quantitative evaluation:[8][4]

- CAGR (Compounded Annual Growth Rate)  
- Annualised volatility  
- Sharpe and Sortino ratios  
- Maximum drawdown and drawdown duration  
- Profit factor and win rate  
- Monthly return breakdown and equity curve

Example (replace with your actual results):

| Metric        | Value    |
|--------------|----------|
| Total Return | +31.94%  |
| CAGR         | 7.19%    |
| Sharpe Ratio | 0.70     |
| Max Drawdown | -9.80%   |
| Win Rate     | 73%      |
| Profit Factor| 1.56     |

***

## Dashboard

The Streamlit app provides an interactive front-end for exploring strategies and results.[6][5]

- Interactive equity curve and drawdown charts  
- Strategy comparison view across key metrics  
- Ticker, strategy, and parameter selection from the UI  
- Raw data preview and historical backtest results loaded from SQLite

Run the dashboard from the project root:

```bash
streamlit run src/quant_trading_strategy_backtester/app_v2.py
```

***

## Installation

```bash
git clone <your-repo-url>
cd quant-trading-strategy-backtester

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
# source venv/bin/activate

pip install -r requirements.txt
```

This setup mirrors typical Python backtesting projects using virtual environments and requirements files.[10][3]

***

## Running a Sample Backtest

From the project root:

```bash
python run_backtest.py
```

This will:

- Fetch historical data for the configured ticker(s)  
- Run the selected strategy and compute metrics  
- Save the equity curve plot to `assets/equity_curve.png`  
- Print performance metrics to the console[1]

You can then open the Streamlit dashboard to inspect results interactively.

***

## Project Structure

```text
quant-trading-strategy-backtester/
├─ src/quant_trading_strategy_backtester/
│  ├─ backtester.py          # Core backtesting engine
│  ├─ data.py                # Data loading via yfinance
│  ├─ models.py              # ORM models for SQLite (SQLAlchemy)
│  ├─ strategies/
│  │  ├─ base.py             # Strategy base class
│  │  ├─ moving_average_crossover.py
│  │  ├─ rsi_strategy.py
│  │  └─ mean_reversion.py
│  ├─ optimiser.py           # Parameter search/optimisation utilities
│  ├─ visualisation.py       # Plotting and analytics helpers
│  └─ app_v2.py              # Streamlit dashboard
├─ tests/                    # pytest-based unit tests
├─ run_backtest.py           # CLI entrypoint for backtests
├─ requirements.txt          # Python dependencies
└─ assets/
   └─ equity_curve.png       # Sample equity curve output
```

This structure follows common patterns used in production-grade backtesting libraries.[11][10]

***

## Usage Examples

- Run a moving average crossover backtest on a single ticker  
- Optimise lookback windows for MA crossover using `optimiser.py`  
- Compare RSI and mean reversion strategies across multiple tickers in the dashboard  
- Inspect stored runs in SQLite to analyse robustness across time frames[2][8]

(You can add concrete code snippets here, such as how to define a new strategy class, once your API is final.)

***

## Roadmap

Planned future enhancements:

- Multi-asset portfolio backtesting and position sizing  
- Transaction cost and slippage modelling  
- Walk-forward and out-of-sample optimisation  
- PDF or HTML export of backtest reports  
- Deployment of the Streamlit dashboard online (e.g., Streamlit Cloud or similar)[6][1]

***

## How to Mention on Your Resume

Example bullet points:

- Built a modular quantitative trading backtesting engine in Python (Polars, Pandas) with multiple strategies, parameter optimisation, and institutional-grade performance analytics (Sharpe, Sortino, drawdowns, CAGR).[4][1]
- Developed an interactive Streamlit dashboard and integrated SQLite + SQLAlchemy for storing, comparing, and visualising historical backtest results.[5][1]

***

## Author

**Author**:Abhilash Reddy Mitta
**Email**: abhilashreddymitta@gmail.com

