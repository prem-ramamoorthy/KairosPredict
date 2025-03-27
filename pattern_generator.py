import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

def find_pips(data: np.array, n_pips: int, dist_measure: int):
    # dist_measure
    # 1 = Euclidean Distance
    # 2 = Perpindicular Distance
    # 3 = Vertical Distance
    pips_x = [0, len(data) - 1]  # Index
    pips_y = [data[0], data[-1]] # Price
    for curr_point in range(2, n_pips):
        md = 0.0 # Max distance
        md_i = -1 # Max distance index
        insert_index = -1
        for k in range(0, curr_point - 1):
            # Left adjacent, right adjacent indices
            left_adj = k
            right_adj = k + 1
            time_diff = pips_x[right_adj] - pips_x[left_adj]
            price_diff = pips_y[right_adj] - pips_y[left_adj]
            slope = price_diff / time_diff
            intercept = pips_y[left_adj] - pips_x[left_adj] * slope;
            for i in range(pips_x[left_adj] + 1, pips_x[right_adj]):
                d = 0.0 # Distance
                if dist_measure == 1: # Euclidean distance
                    d =  ( (pips_x[left_adj] - i) ** 2 + (pips_y[left_adj] - data[i]) ** 2 ) ** 0.5
                    d += ( (pips_x[right_adj] - i) ** 2 + (pips_y[right_adj] - data[i]) ** 2 ) ** 0.5
                elif dist_measure == 2: # Perpindicular distance
                    d = abs( (slope * i + intercept) - data[i] ) / (slope ** 2 + 1) ** 0.5
                else: # Vertical distance    
                    d = abs( (slope * i + intercept) - data[i] )
                if d > md:
                    md = d
                    md_i = i
                    insert_index = right_adj
        pips_x.insert(insert_index, md_i)
        pips_y.insert(insert_index, data[md_i])

    return pips_x, pips_y

def check_trends(points):
    result = [] 
    if len(points) < 2:
        raise ValueError("At least two points are required to compare.")
    for i in range(len(points)):
        try:
            diff = float(points[i+1] - points[i])  # Convert np.float to normal int
            if diff > 0:
                result.append((1,diff))
            elif diff < 0:
                result.append((0,diff))
            else:
                result.append((-1,diff))
        except IndexError:
            break
    return result

def generate_data(stock_name ,time_frame, file) :
    data = pd.read_csv(file)
    data['time'] = data['time'].astype('datetime64[s]')
    data = data.set_index('time')
    i = 0
    e = 70
    pattern_no = 1
    result = []
    while True :
        try:
            segment = data.iloc[i:e]
            segment.to_csv(f'stock_data\\stock_pattern\\{stock_name}\\{time_frame}\\{stock_name}_{pattern_no}.csv')
            x = data['close'].iloc[i:e].to_numpy()
            pips_x, pips_y = find_pips(x,8, 3)
            l=check_trends(pips_y)
            result.append({pattern_no:l})
            i+=70
            e+=70
            pattern_no+=1
        except Exception as e:
            break
    return result

def convert_to_csv(data,s_name , time_frame):
    output_file = f"stock_data\\generated_data\\{s_name}_{time_frame}.csv"
    # Define the header
    header = ['pid', 'ud1', 'ud1_d', 'ud2', 'ud2_d', 'ud3', 'ud3_d', 'ud4', 'ud4_d', 
              'ud5', 'ud5_d', 'ud6', 'ud6_d', 'ud7', 'ud7_d']

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) 
        for pid, trends in data.items():
            row = [pid]
            for trend in trends:
                row.extend(trend)
            writer.writerow(row)

if __name__ == "__main__" : 
    data = generate_data("TSLA", "1D", "historical_data\BATS_TSLA, 1D_875c4.csv")
    combined_data = {}
    for d in data:
        combined_data.update(d)
    convert_to_csv(combined_data,"TSLA", "1D")