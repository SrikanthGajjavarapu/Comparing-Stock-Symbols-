from stock import Stock
from benchmark import Benchmark
from portfolio import Portfolio
import streamlit as st

def main():
    #Symbols
    symbol_reliance = 'RELIANCE.NS'
    symbol_hcltech = 'HCLTECH.NS'
    symbol_tatamotors = 'TATAMOTORS.NS'
    symbol_mnm = 'M&M.NS'
    symbol_eichermot = 'EICHERMOT.NS'
    symbol_jswsteel = 'JSWSTEEL.NS'
    symbol_bajfinance = 'BAJFINANCE.NS'
    symbol_apollohosp = 'APOLLOHOSP.NS'
    symbol_wipro = 'WIPRO.NS'
    symbol_adanient = 'ADANIENT.NS'
    symbol_nifty = '^NSEI'

    start_date = '2019-01-01'
    end_date = '2024-01-01'

    # Creating instances of the Stock class for each stock
    reliance_stock = Stock(symbol_reliance, start_date, end_date)
    hcltech_stock = Stock(symbol_hcltech, start_date, end_date)
    tatamotors_stock = Stock(symbol_tatamotors, start_date, end_date)
    mnm_stock = Stock(symbol_mnm, start_date, end_date)
    eichermot_stock = Stock(symbol_eichermot, start_date, end_date)
    jswsteel_stock = Stock(symbol_jswsteel, start_date, end_date)
    bajfinance_stock = Stock(symbol_bajfinance, start_date, end_date)
    apollohosp_stock = Stock(symbol_apollohosp, start_date, end_date)
    wipro_stock = Stock(symbol_wipro, start_date, end_date)
    adanient_stock = Stock(symbol_adanient, start_date, end_date)

    # Creating an instance of the Benchmark class
    nifty_benchmark = Benchmark(symbol_nifty, start_date, end_date)

    # Creating a list of stocks for the portfolio
    stocks = [reliance_stock, hcltech_stock, tatamotors_stock, mnm_stock, eichermot_stock,
              jswsteel_stock, bajfinance_stock, apollohosp_stock, wipro_stock, adanient_stock]

    # Creating an instance of the Portfolio class
    portfolio = Portfolio(stocks, nifty_benchmark, start_date, end_date)

    #Specific date for analysis
    analysis_date = '2023-12-26'

    #select_portfolio to get selected stocks
    selected_stocks, n_day_returns = portfolio.select_portfolio(analysis_date)
    print(f"Selected Stocks on {analysis_date}: {[stock.symbol for stock in selected_stocks]}")
    print(f"N-day Returns: {n_day_returns}")

    #summarize_performance to get performance metrics
    portfolio.summarize_performance()
    portfolio.visualize_equity_curves()
    
if __name__ == "__main__":
    main()
