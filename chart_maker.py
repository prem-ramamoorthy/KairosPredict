import mplfinance as mpf
import pandas as pd
import threading
import matplotlib.pyplot as plt
import json
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sample_data = pd.read_csv("sample_data.csv")
data = pd.DataFrame({
        'Date': pd.to_datetime(sample_data['time'], unit='s'),
        'Open': sample_data["open"],
        'High': sample_data["high"],
        'Low': sample_data["low"],
        'Close': sample_data["close"],
        'Volume': sample_data["Volume"]
    }).set_index('Date')

def load_colors(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def plot_advanced_candlestick(chart_type ,data , window ,timeframe ):
    global canvas
    ax_candle.clear()
    ax_volume.clear()
    mpf.plot(data, type=chart_type , style=style, ax=ax_candle, volume=ax_volume)
    if canvas is None:
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    else:
        canvas.draw()

def plot_async(chart_type , data1 , window , timeframe):
    print( chart_type , data1 , window , timeframe )
    threading.Thread(target=lambda :plot_advanced_candlestick("candle", data , window , timeframe), daemon=True).start()

def update_configuration():
    global chart_configuration , mc , grid_styles ,style 
    chart_configuration = load_colors("chart_configuration")
    mc = mpf.make_marketcolors(
    up=chart_configuration[0], down=chart_configuration[1],
    wick={'up': chart_configuration[2], 'down': chart_configuration[3]},
    edge={'up': chart_configuration[4], 'down': chart_configuration[5]},
    volume={'up': chart_configuration[6], 'down': chart_configuration[7]}
    )
    grid_styles = {"Dashed line": "--", "Dash-dot line": "-.", "Dotted line": ":", "Solid line": "-"}
    chart_configuration[11] = grid_styles.get(chart_configuration[11], "-")
    style = mpf.make_mpf_style(
    marketcolors=mc,
    gridcolor=chart_configuration[10],
    gridstyle=chart_configuration[11],
    facecolor=chart_configuration[8],
    edgecolor=chart_configuration[9]
    )



if "__name__" == "__main__" :

    chart_configuration = load_colors("chart_configuration")
    

    fig, (ax_candle, ax_volume) = plt.subplots(2, 1, figsize=(6,4), gridspec_kw={'height_ratios': [5, 2]})
    canvas = None

    mc = mpf.make_marketcolors(
        up=chart_configuration[0], down=chart_configuration[1],
        wick={'up': chart_configuration[2], 'down': chart_configuration[3]},
        edge={'up': chart_configuration[4], 'down': chart_configuration[5]},
        volume={'up': chart_configuration[6], 'down': chart_configuration[7]}
    )

    grid_styles = {"Dashed line": "--", "Dash-dot line": "-.", "Dotted line": ":", "Solid line": "-"}
    chart_configuration[11] = grid_styles.get(chart_configuration[11], "-")
    style = mpf.make_mpf_style(
        marketcolors=mc,
        gridcolor=chart_configuration[10],
        gridstyle=chart_configuration[11],
        facecolor=chart_configuration[8],
        edgecolor=chart_configuration[9]
    )