# %% Visualize Plotly in Flask App
# %%
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
# from flask_ngrok import run_with_ngrok 

app = Flask(__name__)
# run_with_ngrok(app) 


@app.route('/')
def chart():
   # import yfinance as yf
   # import plotly.graph_objects as go


   # # Define the ticker symbol
   # ticker_symbol = "AAPL"

   # # Create a Ticker object
   # ticker = yf.Ticker(ticker_symbol)

   # # Fetch historical market data
   # data = ticker.history(period="1y")  # data for the last year
   # print(data)

   # Visualize stock data using Plotly
   # fig = go.Figure(data=[go.Candlestick(x=data.index,
   #                open=data['Open'],
   #                high=data['High'],
   #                low=data['Low'],
   #                close=data['Close'])])

   # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   # return render_template('test.html', graphJSON=graphJSON)
   return render_template('test.html')


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)

# %%
