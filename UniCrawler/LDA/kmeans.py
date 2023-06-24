import os
import json
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances

import nltk
import string

import matplotlib.pyplot as plt


def apply_lda(fname):
    content = list()
    # open file
    try:
        with open(fname) as f:
            data = json.load(f)

    except Exception as e:
        print(f"beim Öffnen von {fname} ist ein Fehler aufgetreten")
        print(f"Fehlermeldung: {e}")

    # check json format
    if isinstance(data, list):
        print(f"{fname} entspricht dem richtigen JSON Format")

        all_text = []

        for i in data:
            if isinstance(i, dict):
                helpList = list()
                helpDict = dict()
                for e in i['paragraphs']:
                    helpList.append(e)
                all_text.extend(helpList)

                helpDict['stud_url'] = i['stud_url']
                helpDict['title'] = i['title']
                content.append(helpDict)

            else:
                print(f"Listenelement ist kein Dict: {type(i)}")
    else:
        print(f"{fname} ist keine gültige JSON.")

    if content:
        tf_idf_vectorizor = TfidfVectorizer(  # tokenizer = tokenize_and_stem,
            max_features=20000)
        tf_idf = tf_idf_vectorizor.fit_transform(all_text)
        tf_idf_norm = normalize(tf_idf)
        tf_idf_array = tf_idf_norm.toarray()

        # Training LDA-Modell
        sklearn_pca = PCA(n_components=2)
        Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)

        # Create the k-means clustering model
        kmeans_model = KMeans(n_clusters=2, max_iter=600, algorithm='lloyd')
        fitted = kmeans_model.fit(Y_sklearn)
        prediction = kmeans_model.predict(Y_sklearn)

        plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], c=prediction, s=50, cmap='viridis')


        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.title(fname)
        output_dir = "./Plot/Kmeans"
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(fname)
        output_filename = os.path.join(output_dir, f"{filename}_kmeansplot2.png")
        plt.savefig(output_filename)
        plt.close()

        def get_top_features_cluster(tf_idf_array, prediction, n_feats):
            labels = np.unique(prediction)
            dfs = []
            for label in labels:
                id_temp = np.where(prediction == label)  # indices for each cluster
                x_means = np.mean(tf_idf_array[id_temp], axis=0)  # returns average score across cluster
                sorted_means = np.argsort(x_means)[::-1][:n_feats]  # indices with top 20 scores
                features = tf_idf_vectorizor.get_feature_names_out()
                best_features = [(features[i], x_means[i]) for i in sorted_means]
                df = pd.DataFrame(best_features, columns=['features', 'score'])
                dfs.append(df)
            return dfs

        dfs = get_top_features_cluster(tf_idf_array, prediction, 15)

    else:
        print(f"Content is empty, something went wrong with:{fname}")


def write_json(fname, content):
    with open(fname, 'w') as f:
        json.dump(content, f)
        print(f"JSON Datei {fname} erfolgreich erstellt")


for root, dirs, files in os.walk('../Resources/Cleaned'):
    if root == "../Resources/Cleaned":
        for file in files:
            # check for json file
            if (file.endswith('.json')):
                fname = root + '/' + file
                apply_lda(fname)
            else:
                print(f"{file} has no json extension.")
    print("finished, no more json files")
