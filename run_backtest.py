import datetime
from quant_trading_strategy_backtester.backtester import Backtester
# from quant_trading_strategy_backtester.strategies.moving_average_crossover import MovingAverageCrossoverStrategy
from quant_trading_strategy_backtester.strategies.rsi_strategy import RSIStrategy

from quant_trading_strategy_backtester.data import load_yfinance_data_one_ticker

# Step 1: Load data
ticker = "AAPL"

data = load_yfinance_data_one_ticker(
    ticker,
    start_date=datetime.date(2020, 1, 1),
    end_date=datetime.date(2023, 12, 31)
)

params = {"window": 14, "lower": 30, "upper": 70}
strategy = RSIStrategy(params)


# Step 4: Run the backtest
bt = Backtester(data, strategy)
results = bt.run()

# Step 5: Print performance metrics
print("\n=== Performance Metrics ===")
metrics = bt.get_performance_metrics()
for k, v in metrics.items():
    print(f"{k}: {v}")

# Step 6: Save results
bt.save_results()
bt.plot_equity_curve("equity_curve.png")

print("\nBacktest complete! Results saved.")

