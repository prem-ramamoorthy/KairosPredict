import mplfinance as mpf
import pandas as pd

def plot_advanced_candlestick(data):
    """
    Plots an advanced TradingView-like candlestick chart using mplfinance.

    Parameters:
    - data (pd.DataFrame): Data with columns ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    
    The 'Date' column should be in datetime format.
    """
    # Ensure Date is the index
    data.set_index('Date', inplace=True)

    # Define moving averages
    ma_short = data['Close'].rolling(window=10).mean()  # Short-term SMA
    ma_long = data['Close'].rolling(window=50).mean()   # Long-term SMA

    # Define styles
    mc = mpf.make_marketcolors(
        up='green', down='red',
        wick={'up': 'lime', 'down': 'red'},  # Wick colors
        edge={'up': 'green', 'down': 'red'},  # Candlestick border colors
        volume={'up': 'green', 'down': 'red'}  # Volume bar colors
    )

    s = mpf.make_mpf_style(
        marketcolors=mc, 
        gridcolor='gray', 
        gridstyle="--",
        facecolor="white", 
        edgecolor="black"
    )

    # Plot candlestick chart with moving averages and volume
    mpf.plot(
        data,
        type='candle',
        style=s,
        volume=True,
        mav=(10, 50),  # Include 10-day and 50-day moving averages
        title="Advanced TradingView-Style Candlestick Chart",
        ylabel="Price",
        ylabel_lower="Volume",
        figratio=(16, 8),  # Adjust figure size
        figscale=1.2  # Scale up the figure
    )

# Example data
data = pd.DataFrame({
    'Date': pd.date_range(start='2024-03-01', periods=10, freq='D'),
    'Open': [100, 102, 104, 101, 103, 107, 106, 109, 111, 110],
    'High': [105, 107, 108, 106, 110, 112, 113, 114, 115, 116],
    'Low': [98, 99, 101, 100, 102, 105, 104, 108, 109, 108],
    'Close': [103, 105, 102, 104, 107, 109, 110, 113, 112, 115],
    'Volume': [102, 100, 101 , 100 , 99 , 98 , 112 , 120 , 113 , 112 ]
})

plot_advanced_candlestick(data)
