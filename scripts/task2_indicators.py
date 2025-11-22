import yfinance as yf
import talib
import pandas as pd
import matplotlib.pyplot as plt
from pynance.indicators import sma, rsi  # Or use TA-Lib directly

# Sample top stocks from EDA (run after notebook)
# Replace with df['stock'].value_counts().index[:2]
top_stocks = ['AAPL', 'GOOGL']

for ticker in top_stocks:
    data = yf.download(ticker, start='2023-01-01', progress=False)
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
    data['RSI_14'] = talib.RSI(data['Close'], timeperiod=14)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data['Close'], label='Close Price')
    ax.plot(data['SMA_20'], label='20-Day SMA')
    ax2 = ax.twinx()
    ax2.plot(data['RSI_14'], color='orange', label='RSI (14)')
    ax.set_title(f'{ticker}: Price & Indicators')
    ax.legend(loc='upper left')
    plt.savefig(f'../reports/{ticker}_indicators.png')
    plt.close()
    print(f"{ticker} RSI mean: {data['RSI_14'].mean():.2f} (neutral if ~50)")

# PyNance example (if installed)
# from pynance import pe_ratio
# data['PE'] = pe_ratio(data)  # Apply to Close/earnings if avail
