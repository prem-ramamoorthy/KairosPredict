import requests
import pandas as pd

API_KEY = "QP8YX4WAKQDDMBRR"
TIMEFRAME_MAPPING = {
    "1m": ("1min", "TIME_SERIES_INTRADAY"),
    "5m": ("5min", "TIME_SERIES_INTRADAY"),
    "15m": ("15min", "TIME_SERIES_INTRADAY"),
    "30m": ("30min", "TIME_SERIES_INTRADAY"),
    "1h": ("60min", "TIME_SERIES_INTRADAY"),
    "1d": (None, "TIME_SERIES_DAILY_ADJUSTED"),
    "1w": (None, "TIME_SERIES_WEEKLY"),
    "1mo": (None, "TIME_SERIES_MONTHLY")
}

def get_live_stock_data(symbol, interval, output_size="compact", save_json=True):
    if interval not in TIMEFRAME_MAPPING:
        print(f"Error: Unsupported interval '{interval}'. Choose from {list(TIMEFRAME_MAPPING.keys())}.")
        return None
    av_interval, function = TIMEFRAME_MAPPING[interval]
    url = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": output_size
    }
    if av_interval: 
        params["interval"] = av_interval
    response = requests.get(url, params=params)
    data = response.json()
    if function == "TIME_SERIES_INTRADAY":
        key = f"Time Series ({av_interval})"
    elif function == "TIME_SERIES_DAILY_ADJUSTED":
        key = "Time Series (Daily)"
    elif function == "TIME_SERIES_WEEKLY":
        key = "Weekly Time Series"
    elif function == "TIME_SERIES_MONTHLY":
        key = "Monthly Time Series"
    else:
        print("Error: Unexpected function type.")
        return None
    print(data)
    if key not in data:
        print(f"Error: No data available. Check API key, stock symbol, or rate limits.")
        return None
    time_series = data[key]
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    }, inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    csv_filename = f"{symbol}_{interval}.csv"
    df.to_csv(csv_filename)
    print(f"Data saved to {csv_filename}")
    return df

stock_symbol = "AAPL"
interval = "1m"
live_data = get_live_stock_data(stock_symbol, interval)
