import os
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import PCA


# expected dummy data for 2 bachelor programs
content = [
    "web",
    "app", "games", "informatik", "programmieren", "vr", "ar", "entwicklung", "anwendung",
    "medieninformatik", "computerspiel", "mediengestaltung", "datenbanksysteme",
    "algorithmen", "ki",
    "software",

    "atmosph\u00e4re boden",
    "tier",
    "methoden",
    "umweltverschmutzung",
    "umweltbildung",
    "artenkenntnis",
    "landschafts\u00f6kologie geobotanik",
    "klimatologie",
    "landschaftsplanung",
    "land"
]

'''
playaround function to test different plots.
LDA + PCA 

'''


def plotPy(content):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(content)

    # Training LDA-Modell
    num_topics = 2
    lda_model = LatentDirichletAllocation(n_components=num_topics)
    X_topics = lda_model.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_topics)

    # Get the dominant topic for each document
    dominant_topics = np.argmax(X_topics, axis=1)

    # colors for diff topics
    colors = ['green', 'orange', 'purple', 'blue', 'red']

    # Visualize the clusters
    plt.scatter(X_pca[:, 0], X_pca[:, 1], s=50, c=[colors[i] for i in dominant_topics])
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title("htw")

    for i, word in enumerate(content):
        plt.annotate(word, (X_pca[i, 0], X_pca[i, 1]))

    plt.show()


plotPy(content)
