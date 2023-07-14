import yfinance as yf
import json
import matplotlib.pyplot as plt
import pandas as pd


def main():
    user_ticker = input("Please input stock Ticker: ").upper()
    stock = yf.Ticker(user_ticker)

    all_info = (stock.get_info())
    current_market = all_info["regularMarketOpen"]
    prev_close = all_info["regularMarketPreviousClose"] 

    print (f"Market Price: {current_market}")
    print(f"Previous Close Price: {prev_close}")

    ask_for_graph = input("Show historical price data? (Y/N) ").upper()
    if ask_for_graph == "Y":
        graph(stock, user_ticker)
    else:
        quit



def graph(stock, ticker):
    history = (stock.history(period="max"))

    open = history["Open"]
    graph = open.plot(title=ticker)
    graph.set_ylabel = open
    graph.grid()
    plt.show()


if __name__ == "__main__":
    main()





