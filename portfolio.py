from stock import Stock
from benchmark import Benchmark
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, stocks, benchmark, start_date, end_date):
        #initializing the Portfolio object
        self.stocks = stocks
        self.benchmark = benchmark
        self.start_date = start_date
        self.end_date = end_date

    def select_portfolio(self, cur_date):
        selected_stocks = []
        l = []

        for stock in self.stocks:
            n_day_return = stock.n_day_ret(30, cur_date)

            # Check if n_day_return is not None and greater than 0
            if n_day_return is not None and n_day_return > 0:
                selected_stocks.append(stock)
                l.append(n_day_return)

        return selected_stocks, l

    def calculate_cagr(self, equity_curve):
        start_value = equity_curve.iloc[0]
        end_value = equity_curve.iloc[-1]
        num_years = len(equity_curve) / 252  # Assuming 252 trading days in a year

        cagr = (end_value / start_value) ** (1 / num_years) - 1
        return cagr

    def summarize_performance(self):
        # Getting the benchmark equity curve
        benchmark_curve = self.benchmark.get_equity_curve()

        # Initializing lists to store daily returns for benchmark and portfolio
        benchmark_daily_returns = benchmark_curve.pct_change().dropna()
        portfolio_daily_returns = []

        # Calculating daily returns for each stock in the portfolio
        for stock in self.stocks:
            stock_returns = stock.historical_data['Close'].pct_change().dropna()
            portfolio_daily_returns.append(stock_returns)

        # Converting the list of portfolio returns to a DataFrame
        portfolio_daily_returns = pd.concat(portfolio_daily_returns, axis=1)

        # Calculating portfolio returns as the mean of individual stock returns
        portfolio_returns = portfolio_daily_returns.mean(axis=1)

        # Calculating CAGR for benchmark and portfolio
        benchmark_cagr = ((benchmark_curve.iloc[-1] / benchmark_curve.iloc[0]) ** (252 / len(benchmark_curve))) - 1
        portfolio_cagr = ((portfolio_returns + 1).prod() ** (252 / len(portfolio_returns))) - 1

        # Calculating volatility for benchmark and portfolio
        benchmark_volatility = benchmark_daily_returns.std() * np.sqrt(252)
        portfolio_volatility = portfolio_returns.std() * np.sqrt(252)

        # Calculating Sharpe Ratio for benchmark and portfolio
        benchmark_sharpe_ratio = (benchmark_cagr / benchmark_volatility)
        portfolio_sharpe_ratio = (portfolio_cagr / portfolio_volatility)

        print("Benchmark CAGR: {:.2%}".format(benchmark_cagr))
        print("Portfolio CAGR: {:.2%}".format(portfolio_cagr))

        print("\nBenchmark Volatility: {:.2%}".format(benchmark_volatility))
        print("Portfolio Volatility: {:.2%}".format(portfolio_volatility))

        print("\nBenchmark Sharpe Ratio: {:.4f}".format(benchmark_sharpe_ratio))
        print("Portfolio Sharpe Ratio: {:.4f}".format(portfolio_sharpe_ratio))
  
    #data visualization curve
    def visualize_equity_curves(self):
        plt.figure(figsize=(10, 6))

        benchmark_curve = self.benchmark.get_equity_curve()
        benchmark_curve.plot(label='Benchmark (Nifty50)', linewidth=2)

        for stock in self.stocks:
            stock_equity_curve = stock.historical_data['Close'] / stock.historical_data['Close'].iloc[0]
            stock_equity_curve.plot(label=stock.symbol, alpha=0.8)

        plt.title('Equity Curves')
        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.legend()
        plt.grid(True)
        plt.show()

