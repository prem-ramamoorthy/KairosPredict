from email import message
import time
from tkinter import messagebox
import pandas as pd
import numpy as np
import threading
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import os
from pattern_generator import generate_data
from data_path import *

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def perform_clustering(df, method='kmeans', n_clusters=10):
    feature_cols = [f'ud{i}' for i in range(1, 8)]
    if method == 'kmeans':
        model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    elif method == 'dbscan':
        model = DBSCAN(eps=0.5, min_samples=5)
    elif method == 'agglomerative':
        model = AgglomerativeClustering(n_clusters=n_clusters)
    else:
        raise ValueError("Unsupported clustering method")  
    df['cluster'] = model.fit_predict(df[feature_cols])
    joblib.dump(model, f'clusters\\cluster_models\\{method}_model.pkl')
    df.to_csv(f'clusters\\cluster_Data\\clustered_data_{method}.csv', index=False)
    return df

def train_cluster_classifier(method):
    df = pd.read_csv(f'clusters\\cluster_Data\\clustered_data_{method}.csv')
    feature_cols = [f'ud{i}' for i in range(1, 8)]
    X = df[feature_cols]
    y = df['cluster']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, f'clusters\\classifiers\\cluster_classifier_{method}.pkl')
    return model

def find_closest_match(new_point, df, classifier_models, distance_metric='euclidean'):
    feature_cols = [f'ud{i}' for i in range(1, 8)]
    new_point_df = pd.DataFrame([new_point[feature_cols]], columns=feature_cols)
    cluster_preds = [model.predict(new_point_df)[0] for model in classifier_models]
    """for i, model in enumerate(classifier_models):
        print(f"Model {i + 1} ({model}): Predicted cluster {cluster_preds[i]}")"""
    cluster_pred = max(set(cluster_preds), key=cluster_preds.count)
    if 'cluster' not in df.columns:
        raise KeyError("The 'cluster' column is missing in the DataFrame. Ensure clustering was performed correctly.")
    cluster_df = df[df['cluster'] == cluster_pred]
    if cluster_df.empty:
        raise ValueError(f"No data found for predicted cluster {cluster_pred}")
    distance_cols = [f'ud{i}_d' for i in range(1, 8)]
    new_point_distances = new_point[distance_cols]

    if distance_metric == 'euclidean':
        distances = euclidean_distances([new_point_distances], cluster_df[distance_cols])
    elif distance_metric == 'manhattan':
        distances = np.abs(cluster_df[distance_cols] - new_point_distances).sum(axis=1).values.reshape(-1, 1)
    elif distance_metric == 'cosine':
        cluster_norms = np.linalg.norm(cluster_df[distance_cols], axis=1)
        new_point_norm = np.linalg.norm(new_point_distances)
        distances = 1 - np.dot(cluster_df[distance_cols], new_point_distances) / (cluster_norms * new_point_norm)
        distances = distances.reshape(-1)  # Ensure distances is a 1D array
    else:
        raise ValueError(f"Unsupported distance metric: {distance_metric}")

    closest_idx = np.argmin(distances)
    return cluster_df.iloc[closest_idx]['pid']

def main(methods=['kmeans', 'dbscan', 'agglomerative'] , distance_metric='euclidean' , visualize_cluster=False , nclusters=10 , stock_name='AAPL', time_frame=' 1d '):
    data = generate_data(stock_name  , time_frame)
    if time_frame != ' 1d ':
        print("Im here ")
        messagebox.showwarning("Warning","This script currently works only for the '1d' time frame.") 
        return
    filepath = f'stock_data\\generated_data\\{stock_name}_{time_frame.strip()}.csv'
    df = load_data(filepath)
    clustered_dfs = {}
    threads = []
    for method in methods:
        t = threading.Thread(target=lambda m, n: clustered_dfs.update({m: perform_clustering(df.copy(), m, n)}), args=(method, nclusters))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    df = clustered_dfs[methods[0]]
    threads = []
    for method in methods:
        t = threading.Thread(target=train_cluster_classifier, args=(method,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    classifier_models = [joblib.load(f'clusters\\classifiers\\cluster_classifier_{method}.pkl') for method in methods]
    new_data = {
        'ud1': data[0][0], 'ud2': data[1][0], 'ud3': data[2][0], 'ud4': data[3][0], 'ud5': data[4][0], 'ud6': data[5][0], 'ud7': data[6][0],
        'ud1_d': data[0][1], 'ud2_d': data[1][1], 'ud3_d':data[2][1], 'ud4_d': data[3][1], 'ud5_d': data[4][1], 'ud6_d': data[5][1], 'ud7_d': data[6][1]
    }
    new_data = pd.Series(new_data)
    pid = find_closest_match(new_data, df, classifier_models , distance_metric=distance_metric)
    vpath = f"stock_data\\stock_pattern\\{stock_name}\\{time_frame.strip()}\\{stock_name}_{int(pid)}.csv"
    set_data_path(vpath)
    print(f'Predicted Pattern ID using Ensemble Method: {pid}')
    if visualize_cluster:
        for method in methods:
            visualize_clusters(method)
    return pid

def visualize_clusters(method):
    try:
        df = pd.read_csv(f'clusters\\cluster_Data\\clustered_data_{method}.csv')
        if 'cluster' not in df.columns:
            raise KeyError(f"'cluster' column not found in clustered data for {method}.")
        feature_cols = [f'ud{i}' for i in range(1, 8)]  # Feature columns only
        pca = PCA(n_components=2)  # Reduce to 2D for visualization
        reduced_data = pca.fit_transform(df[feature_cols])
        df['PCA1'] = reduced_data[:, 0]
        df['PCA2'] = reduced_data[:, 1]
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df['PCA1'], y=df['PCA2'], hue=df['cluster'], palette='tab10', alpha=0.7)
        plt.title(f'Cluster Visualization using {method.upper()} (PCA Reduced)')
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()
    except FileNotFoundError:
        print(f"Error: Clustered data file for {method} not found.")
    except Exception as e:
        print(f"Error: {e}")
    try:
        os.remove(f'clusters\\cluster_Data\\clustered_data_{method}.csv')
    except FileNotFoundError:
        print(f"File not found: clusters\\cluster_Data\\clustered_data_{method}.csv")
    except Exception as e:
        print(f"Error deleting file: {e}")

if __name__ == '__main__':
    main(['kmeans' , 'dbscan', 'agglomerative'], distance_metric='cosine' , visualize_cluster = False , nclusters=15)