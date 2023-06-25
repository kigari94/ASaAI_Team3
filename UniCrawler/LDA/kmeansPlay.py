import os
import json
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.metrics import pairwise_distances

import nltk
import string

import matplotlib.pyplot as plt

content = [
    "web",
    "app", "games", "informatik", "programmieren", "vr", "ar", "entwicklung", "anwendung",
    "medieninformatik", "computerspiel", "mediengestaltung", "datenbanksysteme",
    "algorithmen", "ki",
    "software",    "atmosph\u00e4re boden",
    "tier",
    "methoden",
    "umweltverschmutzung",
    "umweltbildung",
    "artenkenntnis",
    "landschafts\u00f6kologie geobotanik",
    "klimatologie",
    "landschaftsplanung",
    "land",
    "maschinen",
    "wirkzusammenh\u00e4nge",
    "entwicklung",
    "berechnung",
    "konstruktion",
    "mathematik", "physik", " werkstofftechnik",
    "fahrzeugtechnik",
    "fertigung",
]
def plotPykMeans(content):
    tf_idf_vectorizor = TfidfVectorizer(max_features=20000)
    tf_idf = tf_idf_vectorizor.fit_transform(content)
    tf_idf_norm = normalize(tf_idf)
    tf_idf_array = tf_idf_norm.toarray()

    scaler = StandardScaler()
    tf_idf_scaled = scaler.fit_transform(tf_idf_array)

    # Training LDA-Modell
    sklearn_pca = PCA(n_components=3)
    Y_sklearn = sklearn_pca.fit_transform(tf_idf_scaled)

    # Create the k-means clustering model
    kmeans_model = KMeans(n_clusters=3, max_iter=600, algorithm='lloyd')
    fitted = kmeans_model.fit(Y_sklearn)
    prediction = kmeans_model.predict(Y_sklearn)

    plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], c=prediction, s=50, cmap='viridis')

    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title("htw kmeans")
    plt.show()

    # funktion bewertet top wörter in einem cluster und ballert die in n dataframe
    # hier n bissche witzlos, weil alle wörter wichtig sind
    # ist auch von einer Website, deren Tab ich geschlossen hab x_x
    def get_top_features_cluster(tf_idf_array, prediction, n_feats):
        labels = np.unique(prediction)
        dfs = list()
        for label in labels:
            id_temp = np.where(prediction == label)  # indices for each cluster
            x_means = np.mean(tf_idf_array[id_temp], axis=0)  # returns average score across cluster
            sorted_means = np.argsort(x_means)[::-1][:n_feats]  # indices with top 20 scores
            features = tf_idf_vectorizor.get_feature_names_out()
            best_features = [(features[i], x_means[i]) for i in sorted_means]
            df = pd.DataFrame(best_features, columns=['features', 'score'])
            dfs.append(df)
        return dfs

    dfs = get_top_features_cluster(tf_idf_array, prediction, 20)
    print(dfs, "ahhhhhhhh")


plotPykMeans(content)