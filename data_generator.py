import requests
import pandas as pd

API_KEY = "QP8YX4WAKQDDMBRR"

TIMEFRAME_MAPPING = {
    " 1m ": "1min",
    " 5m ": "5min",
    " 15m ": "15min",
    " 30m ": "30min",
    " 1h ": "60min", 
    " 1d ": "daily"  
}

def get_live_stock_data(symbol, interval, output_size="compact"):
    av_interval = TIMEFRAME_MAPPING[interval]
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY" if "min" in av_interval else "TIME_SERIES_DAILY",
        "symbol": symbol,
        "interval": av_interval if "min" in av_interval else None,
        "apikey": API_KEY,
        "outputsize": output_size
    }
    params = {k: v for k, v in params.items() if v is not None}
    response = requests.get(url, params=params)
    data = response.json()
    key = f"Time Series ({av_interval})" if "min" in av_interval else "Time Series (Daily)"
    if key not in data:
        return False
    time_series = data[key]
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "Volume"
    }, inplace=True)
    df.index = pd.to_datetime(df.index)
    df.index.name = "time"
    df = df.sort_index()
    df.to_csv(f"stock_data\\{symbol}_{interval}_data.csv")
    return True

if __name__ == "__main__":
    stock_symbol = "AAPL"
    time_intervals = [" 1m ", " 5m ", " 15m ", " 30m ", " 1h ", " 1d "]
    live_data = get_live_stock_data(stock_symbol, "1d")
    print(live_data)