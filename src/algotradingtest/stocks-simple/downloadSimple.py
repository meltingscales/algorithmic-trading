# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pyfolio as pf
import datetime as dt
import pandas_datareader.data as web
import os
import warnings

# Ignore printing all warnings
from nbformat import write

warnings.filterwarnings('ignore')

# print all outputs
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

# downloading historical necessary data for backtesting and analysis
_start = dt.date(2015, 1, 2)
_end = dt.date(2020, 4, 30)
ticker = 'MSFT'
df = yf.download(ticker, start=_start, end=_end)

fp = f'./{ticker}-sample.xlsx'
if os.path.exists(fp):
    print(f"{fp} exists.")
    exit(1)

writer = pd.ExcelWriter(fp)
df.to_excel(writer)

writer.save()
print("Done, open " + fp)
