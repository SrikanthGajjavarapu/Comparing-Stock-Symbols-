import yfinance as yf
import pandas as pd

#calculating benchbark on the basis of Nifty 50
class Benchmark:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.historical_data = self.download_data()

    def download_data(self):
        try:
            data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            return data
        except Exception as e:
            print(f"Error downloading data for {self.symbol}: {e}")
            return None

    def get_equity_curve(self):
        try:
            # Assuming 'Close' is the column in historical_data representing closing prices
            equity_curve = self.historical_data['Close'] / self.historical_data['Close'].iloc[0]
            return equity_curve
        except Exception as e:
            print(f"Error calculating benchmark equity curve: {e}")
            return None


