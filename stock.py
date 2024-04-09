import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from datetime import datetime, date

class Stock:
    def __init__(self, symbol, start_date, end_date):
        #initializing the Stock object
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.historical_data = self.download_data()

    def download_data(self):
        # downloading historical stock data
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return data

    def cur_price(self, cur_date):
    #get the closing price for a given date
      try:
          if isinstance(cur_date, date):
              cur_date_str = cur_date.strftime('%Y-%m-%d')
          else:
              cur_date_str = cur_date

          return self.historical_data.loc[cur_date_str]['Close']
      except KeyError:
          print(f"Data not available for {cur_date}")
          return None


    def n_day_ret(self, N, cur_date, max_days_back=5):
      try:
          cur_date = datetime.strptime(cur_date, '%Y-%m-%d')
          cur_date_str = cur_date.strftime('%Y-%m-%d')
          cur_date = pd.to_datetime(cur_date_str).date()

          price_today = self.cur_price(cur_date)

          # Checking price_today is available
          if price_today is None:
              print(f"Data not available for {cur_date}. Skipping this date.")
              return None

          # Initializing a list to store available prices
          available_prices = [price_today]

          # Look for available prices within the specified range
          for days_back in range(1, max_days_back + 1):
              previous_date = cur_date - pd.DateOffset(days=days_back)
              price = self.cur_price(previous_date)

              if price is not None:
                  available_prices.append(price)

          # If no data is available within the range, return None
          if len(available_prices) < 2:
              print(f"Not enough data within the specified range to calculate N-day return for {cur_date}.")
              return None

          # Calculating N-day return for the remaining available dates
          price_today = available_prices[0]
          price_N_days_ago = available_prices[-1]

          return (price_today / price_N_days_ago) - 1

      except ValueError as e:
          print(f"Error calculating N-day return for {cur_date}: {e}")
          return None


    def daily_ret(self, cur_date):
        # Method to get daily returns for a given date
        try:
            cur_date = datetime.strptime(cur_date, '%Y-%m-%d')  # Convert input string to datetime object
            return self.historical_data.loc[cur_date.strftime('%Y-%m-%d')]['Close'] / self.historical_data.loc[(cur_date - pd.DateOffset(days=1)).strftime('%Y-%m-%d')]['Close'] - 1
        except KeyError:
            print(f"Data not available for {cur_date}")
            return None
        except TypeError:
            return None

    def last_30_days_price(self, cur_date):
        # Method to get an array of last 30 days prices
        try:
            cur_date = datetime.strptime(cur_date, '%Y-%m-%d')  # Convert input string to datetime object
            end_date = cur_date - pd.DateOffset(days=1)
            start_date = end_date - pd.DateOffset(days=30)
            return self.historical_data.loc[start_date.strftime('%Y-%m-%d'):end_date.strftime('%Y-%m-%d')]['Close'].values
        except KeyError:
            print(f"Data not available for {cur_date}")
            return None

