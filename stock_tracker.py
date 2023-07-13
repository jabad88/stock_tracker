import yfinance as yf
import json
import matplotlib.pyplot as plt
import pendulum
#test
def main():
    user_ticker = input("Please input stock Ticker: ").upper()
    stock = yf.Ticker(user_ticker)

    all_info = (stock.get_info())
    current_market = all_info["regularMarketOpen"]
    prev_close = all_info["regularMarketPreviousClose"] 

    print (f"Market Price: {current_market}")
    print(f"Previous Close Price: {prev_close}")


if __name__ == "__main__":
    main()





