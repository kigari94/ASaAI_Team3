
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize, StandardScaler
import matplotlib.pyplot as plt

'''
trying to simulate ideal data and plot with kmeans
'''
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

plotPykMeans(content)