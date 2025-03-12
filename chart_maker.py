import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

def load_colors(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

import pandas as pd
import mplfinance as mpf

def plot_advanced_candlestick(data, ax_candle, ax_volume, fig, window):
    chart_configuration = load_colors("chart_configuration")
    data['Date'] = pd.to_datetime(data['Date'])
    data_indexed = data.set_index('Date')
    mc = mpf.make_marketcolors(
        up=chart_configuration[0], down=chart_configuration[1],
        wick={'up': chart_configuration[2], 'down': chart_configuration[3]},
        edge={'up': chart_configuration[4], 'down': chart_configuration[5]},
        volume={'up': chart_configuration[6], 'down': chart_configuration[7]}
    )
    grid_styles = {
        "Dashed line": "--",
        "Dash-dot line": "-.",
        "Dotted line": ":",
        "Solid line": "-",
        "No grid" : ""
    }
    selected_grid_style = grid_styles.get(chart_configuration[11], "")
    s = mpf.make_mpf_style(
        marketcolors=mc,
        gridcolor=chart_configuration[10],
        gridstyle=selected_grid_style,
        facecolor=chart_configuration[8],
        edgecolor=chart_configuration[9]
    )
    fig.patch.set_facecolor(chart_configuration[8]) 
    for ax in [ax_candle, ax_volume]:  
        ax.set_facecolor(chart_configuration[8])  
        for spine in ax.spines.values():
            spine.set_edgecolor(chart_configuration[9])
        ax.grid(color=chart_configuration[10], linestyle=selected_grid_style)
    mpf.plot(
        data_indexed,
        type="candle",
        style=s,
        ax=ax_candle,
        volume=ax_volume
    )
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row= 0, column= 0)