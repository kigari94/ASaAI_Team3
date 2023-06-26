import os
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA

'''
PCA und LDA Plotten aller Daten aus /Resources/Clean
'''


def plot(fname):
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
        # Vectorizing the text
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(all_text)

        # Training LDA-Modell
        num_topics = 5
        lda_model = LatentDirichletAllocation(n_components=num_topics)
        X_topics = lda_model.fit_transform(X)

        # dimension reduction with pca
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_topics)

        # Get the dominant topic for each document
        dominant_topics = np.argmax(X_topics, axis=1)

        # Visualize the clusters
        # if you want to run with PCA
        # plt.scatter(X_pca[:, 0], X_pca[:, 1], c=dominant_topics)
        plt.scatter(X_topics[:, 0], X_topics[:, 1], c=dominant_topics)
        plt.xlabel('Component')
        plt.ylabel('Component')
        plt.title(fname)

        # output
        output_dir = "./Plot"  # Specify the directory path
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(fname)
        output_filename = os.path.join(output_dir, f"{filename}_LDAplot.png")
        plt.savefig(output_filename)
        plt.close()


    else:
        print(f"Content is empty, something went wrong with: {fname}")

for root, dirs, files in os.walk('../Resources/Cleaned'):
    if root == "../Resources/Cleaned":
        for file in files:
            # check for json file
            if (file.endswith('.json')):
                fname = root + '/' + file
                plot(fname)
            else:
                print(f"{file} has no json extension.")
    print("finished, no more json files")
