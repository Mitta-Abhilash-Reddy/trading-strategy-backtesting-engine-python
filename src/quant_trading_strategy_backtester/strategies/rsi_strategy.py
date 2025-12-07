import polars as pl
from quant_trading_strategy_backtester.strategies.base import BaseStrategy

class RSIStrategy(BaseStrategy):
    def __init__(self, params):
        super().__init__(params)
        self.window = params.get("window", 14)
        self.lower = params.get("lower", 30)
        self.upper = params.get("upper", 70)

    def generate_signals(self, data: pl.DataFrame) -> pl.DataFrame:
        close = data["Close"]

        # Price difference
        delta = close.diff()

        # Polars clipping
        gain = delta.clip(lower_bound=0)
        loss = (-delta).clip(lower_bound=0)

        # Rolling averages
        avg_gain = gain.rolling_mean(self.window)
        avg_loss = loss.rolling_mean(self.window)

        # RS + RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        signals = data.with_columns([
            rsi.alias("RSI"),
        ])

        # Generate positions using RSI
        signals = signals.with_columns(
            pl.when(rsi < self.lower)
              .then(1)
              .when(rsi > self.upper)
              .then(0)
              .otherwise(0)
              .alias("positions")
        )

        return signals
