<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Quant Trading Strategy Backtester</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial; color:#0b1726; line-height:1.6; margin:0; padding:0; background:#f7fafc; }
    .container { max-width:900px; margin:40px auto; padding:28px; background:#ffffff; border-radius:12px; box-shadow:0 8px 30px rgba(11,23,38,0.06); }
    header { display:flex; align-items:center; gap:18px; margin-bottom:20px; }
    header img { width:64px; height:64px; object-fit:cover; border-radius:8px; }
    h1 { margin:0; font-size:26px; }
    .subtitle { color:#475569; margin-top:6px; font-size:14px; }
    .badges { margin-top:12px; }
    .badges img { height:20px; margin-right:8px; vertical-align:middle; }
    section { margin-top:22px; }
    h2 { font-size:18px; margin-bottom:12px; color:#0f172a; }
    pre { background:#0b1220; color:#cfe8ff; padding:12px; border-radius:8px; overflow:auto; font-size:13px; }
    code { background:#eef2ff; padding:2px 6px; border-radius:6px; font-family:monospace; }
    ul { margin:0 0 12px 18px; }
    .grid { display:grid; gap:12px; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); }
    .card { background:#f1f5f9; padding:14px; border-radius:10px; border:1px solid #e2e8f0; }
    .metrics { display:flex; gap:12px; flex-wrap:wrap; }
    .metric { background:#fff; padding:10px 12px; border-radius:10px; box-shadow:0 2px 6px rgba(2,6,23,0.04); }
    .footer { color:#64748b; font-size:13px; margin-top:26px; border-top:1px dashed #e6eef7; padding-top:16px; }
    a { color:#0b69ff; text-decoration:none; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <img alt="logo" src="assets/logo.png" onerror="this.style.display='none'"/>
      <div>
        <h1>Quant Trading Strategy Backtester</h1>
        <div class="subtitle">Modular Python backtesting engine with strategies, optimisation, metrics & Streamlit dashboard</div>
        <div class="badges">
          <!-- Replace badges or remove if not available -->
          <img alt="python" src="https://img.shields.io/badge/python-3.8%2B-blue"/>
          <img alt="license" src="https://img.shields.io/badge/license-MIT-brightgreen"/>
        </div>
      </div>
    </header>

    <section>
      <h2>Project Overview</h2>
      <p>
        This repository implements a production-style quantitative backtesting platform written in Python.
        It supports multiple strategies (Moving Average Crossover, RSI, Mean Reversion, Pairs Trading), a
        vectorized returns engine (Polars), an optimisation module, and an interactive Streamlit dashboard to
        visualise results. Results are persisted to a local SQLite database for reproducibility and comparison.
      </p>
    </section>

    <section>
      <h2>Key Features</h2>
      <div class="grid">
        <div class="card">
          <strong>Backtester Engine</strong>
          <ul>
            <li>Vectorized returns & equity curve computation (Polars)</li>
            <li>Pluggable strategy interface (add custom strategies)</li>
            <li>Trade simulation with positions & PnL</li>
          </ul>
        </div>
        <div class="card">
          <strong>Strategies Included</strong>
          <ul>
            <li>Moving Average Crossover</li>
            <li>RSI-based entry/exit</li>
            <li>Mean Reversion</li>
            <li>Pairs Trading</li>
          </ul>
        </div>
        <div class="card">
          <strong>Analytics & Metrics</strong>
          <ul>
            <li>Sharpe, Sortino, CAGR, Max Drawdown</li>
            <li>Profit Factor, Win Rate, # Trades</li>
            <li>Monthly returns and heatmap</li>
          </ul>
        </div>
        <div class="card">
          <strong>Dashboard & Storage</strong>
          <ul>
            <li>Streamlit UI with interactive charts</li>
            <li>SQLite + SQLAlchemy persistence</li>
            <li>Unit tests using pytest (reliability)</li>
          </ul>
        </div>
      </div>
    </section>

    <section>
      <h2>Tech Stack</h2>
      <ul>
        <li><strong>Language:</strong> Python 3.8+</li>
        <li><strong>Data engine:</strong> Polars (fast vectorized operations)</li>
        <li><strong>Data source:</strong> yfinance</li>
        <li><strong>Dashboard:</strong> Streamlit (+ Plotly/Matplotlib for visuals)</li>
        <li><strong>DB:</strong> SQLite via SQLAlchemy</li>
        <li><strong>Testing:</strong> pytest</li>
      </ul>
    </section>

    <section>
      <h2>Install & Quick Start</h2>

      <p>Run the following commands in your project root (tested on Windows/macOS/Linux):</p>

      <pre><code>git clone &lt;your-repo-url&gt;
cd quant-trading-strategy-backtester
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt
# if you used a minimal requirements file, ensure these are present:
# pandas numpy matplotlib yfinance ta scikit-learn polars streamlit sqlalchemy pytest
</code></pre>

      <p>Run unit tests:</p>
      <pre><code>python -m pytest</code></pre>

      <p>Run a quick backtest script (example):</p>
      <pre><code>python run_backtest.py
# outputs saved in results/ and a plot: equity_curve.png
</code></pre>

      <p>Run the Streamlit dashboard (recommended):</p>
      <pre><code>cd &lt;project-root&gt;
streamlit run src/quant_trading_strategy_backtester/app_v2.py
</code></pre>
    </section>

    <section>
      <h2>Usage Examples</h2>

      <h3>Run Moving Average Backtest (example)</h3>
      <pre><code>python run_backtest.py
# or call directly from python:
# from quant_trading_strategy_backtester.backtester import Backtester
# from quant_trading_strategy_backtester.strategies.moving_average_crossover import MovingAverageCrossoverStrategy
# and call Backtester(data, strategy).run()
</code></pre>

      <h3>Run RSI Strategy</h3>
      <pre><code># change params in run_backtest.py to use RSIStrategy
python run_backtest.py
</code></pre>
    </section>

    <section>
      <h2>Project Structure</h2>
      <pre><code>quant-trading-strategy-backtester/
├─ src/quant_trading_strategy_backtester/
│  ├─ backtester.py
│  ├─ data.py
│  ├─ models.py
│  ├─ strategies/
│  │  ├─ base.py
│  │  ├─ moving_average_crossover.py
│  │  ├─ rsi_strategy.py
│  │  └─ ...
│  ├─ optimiser.py
│  ├─ visualisation.py
│  └─ app_v2.py
├─ tests/
├─ run_backtest.py
├─ requirements.txt
├─ README.html
└─ assets/
   └─ equity_curve.png
</code></pre>
    </section>

    <section>
      <h2>Performance Snapshot (Example)</h2>
      <div class="metrics">
        <div class="metric"><strong>Total Return</strong><div>+31.94%</div></div>
        <div class="metric"><strong>CAGR</strong><div>+7.19%</div></div>
        <div class="metric"><strong>Sharpe</strong><div>0.70</div></div>
        <div class="metric"><strong>Max Drawdown</strong><div>-9.80%</div></div>
        <div class="metric"><strong>Win Rate</strong><div>73%</div></div>
      </div>

      <p style="margin-top:12px;">(Replace these values with your real results or include a small table screenshot)</p>

      <div style="margin-top:14px;">
        <img src="assets/equity_curve.png" alt="Equity Curve" style="max-width:100%; border-radius:8px; border:1px solid #e6eef7;" onerror="this.style.display='none'"/>
      </div>
    </section>

    <section>
      <h2>How to Present This on Your Resume</h2>
      <ul>
        <li><strong>Short line:</strong> Built a modular quant backtesting engine in Python (Polars, Streamlit) with strategy optimisation and institutional-grade metrics (Sharpe, Sortino, CAGR).</li>
        <li><strong>Longer bullets:</strong> See the <code>docs/</code> or the project summary in the repo for suggested bullets and screenshots.</li>
      </ul>
    </section>

    <section>
      <h2>Next Steps / Roadmap</h2>
      <ul>
        <li>Add portfolio-level multi-asset backtesting</li>
        <li>Model transaction costs & realistic slippage</li>
        <li>Deploy dashboard to Streamlit Cloud / Heroku</li>
        <li>Export backtest PDF reports and downloadable CSVs</li>
      </ul>
    </section>

    <section class="footer">
      <div>Made with ❤️ by <strong>Your Name</strong> — <a href="mailto:youremail@example.com">youremail@example.com</a></div>
      <div style="margin-top:8px;">License: MIT — see <code>LICENSE</code> for details.</div>
    </section>
  </div>
</body>
</html>
