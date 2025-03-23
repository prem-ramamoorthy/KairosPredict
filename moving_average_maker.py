import re
from unittest import result
import numpy as np
import pandas as pd

def set_moving_average_window(value):
    global moving_average_window
    moving_average_window = value

def simple_moving_average(data, volume, window):
    result = np.convolve(data, np.ones(window)/window, mode='valid')
    return result

def exponential_moving_average(data, volume, window_size):
    result  = pd.Series(data).ewm(span=window_size, adjust=False).mean().to_numpy()
    return result

def weighted_moving_average(data, volume, window):
    weights = np.arange(1, window + 1)
    result = np.convolve(data, weights/weights.sum(), mode='valid')
    return result

def triangular_moving_average(data, volume, window_size):
    if window_size % 2 == 0:
        window_size += 1  # Ensure odd window size
    first_sma = simple_moving_average(data,None , (window_size+ 1) // 2)
    result = simple_moving_average(first_sma, None ,(window_size + 1) // 2 )
    return result

def kaufman_adaptive_moving_average(data, volume, window_size):
    change = np.abs(data[window_size:] - data[:-window_size])
    volatility = np.sum(np.abs(data[1:] - data[:-1]))
    er = change / (volatility + 1e-10)  # Efficiency Ratio
    sc = (er * (2 / (window_size + 1) - 2 / (window_size* 2 - 1)) + 2 / (window_size * 2 - 1)) ** 2
    kama = np.zeros_like(data)
    kama[window_size] = data[window_size]
    for i in range(window_size + 1, len(data)):
        kama[i] = kama[i - 1] + sc[i - window_size] * (data[i] - kama[i - 1])
    return kama[window_size:]

def hull_moving_average(data, volume, window_size):
    wma_half = weighted_moving_average(data,None, window_size // 2)
    wma_full = weighted_moving_average(data, None,window_size)
    diff = 2 * wma_half[:len(wma_full)] - wma_full
    result = weighted_moving_average(diff, None , int(np.sqrt(window_size)))
    return result

def volume_weighted_moving_average(data, volume, window_size):
    price = np.array(data)
    volume = np.array(volume)
    vwma = np.convolve(price * volume, np.ones(window_size), 'valid') / np.convolve(volume, np.ones(window_size), 'valid')
    return vwma

def plot_moving_average(data, volume,window_size=3):
    movingaverage = getmovingaverage()
    try:
        window_size = int(window_size)
        if window_size <= 0:
            raise ValueError
    except (ValueError, TypeError):
        window_size = 3 
    if movingaverage == "Simple Moving Average":
        return simple_moving_average(data, volume, window_size)
    elif movingaverage == "Exponential Moving Average":
        return exponential_moving_average(data, volume, window_size)
    elif movingaverage == "Weighted Moving Average":
        return weighted_moving_average(data, volume, window_size)
    elif movingaverage == "Triangular Moving Average":
        return triangular_moving_average(data, volume, window_size)
    elif movingaverage == "Kaufman Adaptive Moving Average":
        return kaufman_adaptive_moving_average(data, volume, window_size)
    elif movingaverage == "Hull Moving Average":
        return hull_moving_average(data, volume, window_size)
    elif movingaverage == "Volume Weighted Moving Average":
        return volume_weighted_moving_average(data, volume, window_size)
    else:
        return simple_moving_average(data, volume, window_size)

def set_moving_average_on_off(v):
    global moving_average_enabled
    moving_average_enabled = not moving_average_enabled

def get_moving_average_on_off():
    global moving_average_enabled
    return moving_average_enabled

def setmovingaverage(value):
    global movingaverage
    movingaverage = value

def getmovingaverage():
    global movingaverage
    return movingaverage

moving_average_enabled = False
movingaverage = "Simple Moving Average"
moving_average_window = 3