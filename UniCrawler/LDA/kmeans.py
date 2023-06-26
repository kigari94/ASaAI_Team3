import os
import json
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

'''
kmeans using TL-IDF, PCA and k-Means clustering
'''
def kmeans(fname):
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
        # TF-IDF
        tf_idf_vectorizor = TfidfVectorizer(max_features=20000)
        tf_idf = tf_idf_vectorizor.fit_transform(all_text)
        tf_idf_norm = normalize(tf_idf)
        tf_idf_array = tf_idf_norm.toarray()

        # PCA
        sklearn_pca = PCA(n_components=2)
        Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)

        # Create the k-means clustering model choose different cluster
        kmeans_model = KMeans(n_clusters=25, max_iter=600, algorithm='lloyd')
        fitted = kmeans_model.fit(Y_sklearn)
        prediction = kmeans_model.predict(Y_sklearn)

        plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1], c=prediction, s=50, cmap='viridis')


        plt.xlabel('Component1')
        plt.ylabel('Component2')
        plt.title(fname)
        output_dir = "./Plot/Kmeans"
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(fname)
        output_filename = os.path.join(output_dir, f"{filename}_kmeansplot.png")
        plt.savefig(output_filename)
        plt.close()

    else:
        print(f"Content is empty, something went wrong with:{fname}")



for root, dirs, files in os.walk('../Resources/Cleaned'):
    if root == "../Resources/Cleaned":
        for file in files:
            # check for json file
            if (file.endswith('.json')):
                fname = root + '/' + file
                kmeans(fname)
            else:
                print(f"{file} has no json extension.")
    print("finished, no more json files")