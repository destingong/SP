import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config
from taipy import Gui

# from token import NGROK_TOKEN
NGROK_TOKEN = "2rbsysF7VUDlz0D8HdQPRxFkPj3_3kahZiBoKtmgWoLe8Ntij"

import yfinance as yf
import plotly.graph_objects as go

# Define the ticker symbol
ticker_symbol = "AAPL"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data
data = ticker.history(period="1y")  # data for the last year

with tgb.Page() as root_page:
    tgb.navbar()
    tgb.text("# Multi-page application", mode="md")
    tgb.chart("{data}", type="line", x='Date', y="Open")


with tgb.Page() as home_page:
    tgb.text("# Home", mode="md")

with tgb.Page() as about_page:
    tgb.text("# About", mode="md")

pages = {
    "/": root_page,
    "home": home_page,
    "about": about_page
}

Gui(pages=pages).run(
    title='Data Science Dashboard',
    ngrok_token=NGROK_TOKEN
)