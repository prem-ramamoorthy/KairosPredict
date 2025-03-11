import customtkinter as ctk
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample stock data (Date, Open, High, Low, Close, Volume)
data = {
    "Date": pd.date_range(start="2024-03-01", periods=10, freq="D"),
    "Open": [100, 102, 104, 103, 106, 108, 107, 109, 111, 110],
    "High": [105, 106, 107, 108, 110, 111, 112, 114, 115, 116],
    "Low": [98, 100, 102, 101, 104, 106, 105, 108, 109, 108],
    "Close": [102, 104, 103, 106, 108, 107, 109, 111, 110, 112],
    "Volume": [1000, 1200, 1500, 1100, 1700, 1600, 1400, 1800, 2000, 1900],
}
df = pd.DataFrame(data)
df.set_index("Date", inplace=True)
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("700x600")
root.title("Candlestick Chart in CustomTkinter")
def plot_candlestick():
    fig, (ax_candle, ax_volume) = plt.subplots(2, 1, figsize=(6, 4), gridspec_kw={'height_ratios': [3, 1]})
    mpf.plot(df, type="candle", style="charles", ax=ax_candle, volume=ax_volume)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
frame = ctk.CTkFrame(root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
plot_button = ctk.CTkButton(root, text="Plot Candlestick Chart", command=plot_candlestick)
plot_button.pack(pady=10)

root.mainloop()
