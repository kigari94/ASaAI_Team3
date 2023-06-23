import os
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA

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
        # Vektorisierung des Textes
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(all_text)

        # Training LDA-Modell
        num_topics = 5
        lda_model = LatentDirichletAllocation(n_components=num_topics)
        X_topics = lda_model.fit_transform(X)

        # Dimensionalität reduzieren mit PCA
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_topics)

        # Get the dominant topic for each document
        dominant_topics = np.argmax(X_topics, axis=1)

        # Define colors for different topics
        colors = ['red', 'blue', 'green', 'orange', 'purple']

        # Visualize the clusters
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=[colors[i] for i in dominant_topics])
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.title(fname)
        # plt.legend(loc="best", shadow=False, scatterpoints=1)
        output_dir = "./Plot"  # Specify the directory path
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(fname)  # Get the base filename without the path
        output_filename = os.path.join(output_dir, f"{filename}_plot.png")
        plt.savefig(output_filename)
        plt.close()


    else:
        print(f"Content is empty, something went wrong with: {fname}")


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


