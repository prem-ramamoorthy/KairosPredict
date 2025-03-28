import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
from data_generator import get_live_stock_data
from moving_average_maker import plot_moving_average
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from tkinter import filedialog

def load_colors(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def plot_advanced_candlestick(ax_candle, ax_volume, fig, window ,clear , candle_style , time_frame , stock , on_off  , window_size , sample = False):
    ax_candle.clear()
    ax_volume.clear()
    if sample == True:
        sample_data = sample_data = pd.read_csv("stock_data\\sample_data.csv")
    else :
        validity = get_live_stock_data(stock,time_frame, output_size="compact")
        if validity == False :
            print("Data Not genrated !!!")
            sample_data = pd.read_csv("stock_data\\sample_data.csv")
        else :
            sample_data = pd.read_csv(f"stock_data\\{stock}_{time_frame}_data.csv")
    data = pd.DataFrame({
        'Date': sample_data["time"],
        'Open': sample_data["open"],
        'High': sample_data["high"],
        'Low': sample_data["low"],
        'Close': sample_data["close"],
        'Volume': sample_data["Volume"]
    })
    chart_configuration = load_colors("chart_configuration")
    data['Date'] = pd.to_datetime(data['Date'])
    data_indexed = data.set_index('Date')
    mc = mpf.make_marketcolors(
        up=chart_configuration[0], down=chart_configuration[1],
        wick={'up': chart_configuration[2], 'down': chart_configuration[3]},
        edge={'up': chart_configuration[4], 'down': chart_configuration[5]},
        volume={'up': chart_configuration[6], 'down': chart_configuration[3]}
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
    try :
        fig.patch.set_facecolor(chart_configuration[8]) 
        for ax in [ax_candle, ax_volume]:  
            ax.set_facecolor(chart_configuration[8])  
            for spine in ax.spines.values():
                spine.set_edgecolor(chart_configuration[9])
            ax.grid(color=chart_configuration[10], linestyle=selected_grid_style)
        mpf.plot(
            data_indexed,
            type=candle_style,
            style=s,
            ax=ax_candle,
            volume=ax_volume,
        )
        if on_off:
            moving_avg = plot_moving_average(data["Close"], data["Volume"], window_size)
            valid_dates = data.index[-len(moving_avg):]
            ax_candle.plot(valid_dates, moving_avg, color=chart_configuration[7], linestyle='-', linewidth=1.5, label=f"{window_size}-Day MA")
            ax_candle.legend()
        ax_candle.xaxis.set_visible(False)
        fig.subplots_adjust(left=0.1, right=0.98, top=0.98, bottom=0.19, hspace=0.001, wspace=0.001)
        fig.patch.set_edgecolor("black") 
        fig.patch.set_linewidth(2) 
        canvas = FigureCanvasTkAgg(fig, master=window)

        def on_key_press(event):
            try:
                xlim = ax_candle.get_xlim()
                ylim = ax_candle.get_ylim()
                zoom_factor = 0.1
                pan_factor = 0.1

                if event.key == 'a': 
                    ax_candle.set_xlim(xlim[0] - (xlim[1] - xlim[0]) * zoom_factor, xlim[1])
                elif event.key == 'd': 
                    ax_candle.set_xlim(xlim[0] + (xlim[1] - xlim[0]) * zoom_factor, xlim[1])
                elif event.key == 'w': 
                    ax_candle.set_ylim(ylim[0] - (ylim[1] - ylim[0]) * zoom_factor, ylim[1])
                elif event.key == 's':
                    ax_candle.set_ylim(ylim[0] + (ylim[1] - ylim[0]) * zoom_factor, ylim[1])
                elif event.key == 'left': 
                    ax_candle.set_xlim(xlim[0] - (xlim[1] - xlim[0]) * pan_factor, xlim[1] - (xlim[1] - xlim[0]) * pan_factor)
                elif event.key == 'right': 
                    ax_candle.set_xlim(xlim[0] + (xlim[1] - xlim[0]) * pan_factor, xlim[1] + (xlim[1] - xlim[0]) * pan_factor)
                elif event.key == 'up': 
                    ax_candle.set_ylim(ylim[0] + (ylim[1] - ylim[0]) * pan_factor, ylim[1] + (ylim[1] - ylim[0]) * pan_factor)
                elif event.key == 'down': 
                    ax_candle.set_ylim(ylim[0] - (ylim[1] - ylim[0]) * pan_factor, ylim[1] - (ylim[1] - ylim[0]) * pan_factor)
                elif event.key == 'ctrl+s':  
                    file_path = filedialog.asksaveasfilename(
                        defaultextension=".png",
                        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
                    )
                    if file_path:
                        fig.savefig(file_path, dpi=300)
                        print(f"Chart saved as {file_path}")
                canvas.draw()
            except Exception as e:
                print(f"Error during zoom, pan, or save: {e}")

        canvas.mpl_connect("key_press_event", on_key_press)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

    except Exception as e :
        print(e)