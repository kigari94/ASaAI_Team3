import os
import json

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


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
    if type(data) is list:
        print(f"{fname} entspricht dem richtigen JSON Format")

        for i in data:
            # if type(i) is dict:
            if isinstance(i, dict):
                helpList = list()
                helpDict = dict()

                for e in i['paragraphs']:
                    helpList.append(e)
                text = helpList

                # vectorizing the text
                vectorizer = CountVectorizer()
                X = vectorizer.fit_transform(text)

                # initiate LDA-model
                num_topics = 5
                lda_model = LatentDirichletAllocation(n_components=num_topics)
                lda_model.fit(X)

                # print topics
                feature_names = vectorizer.get_feature_names_out()
                tokens = list()
                for topic_idx, topic in enumerate(lda_model.components_):
                    top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
                    tokens.append(', '.join(top_words))

                helpDict['stud_url'] = i['stud_url']
                helpDict['title'] = i['title']
                helpDict['paragraphs'] = tokens

                content.append(helpDict)

            else:
                print(f"Element is not a dict: {type(i)}")
    else:
        print(f"{fname} is not a valid JSON file.")

    if content is not None:
        write_json("../LDA/SkLearnOutput/" + os.path.basename(fname).split("_")[0] + "_sklearn.json", content)
    else:
        print(f"Content is empty, something went wrong with: {fname}")


def write_json(fname, content):
    with open(fname, 'w') as f:
        json.dump(content, f)
        print(f"JSON file {fname} was generated.")


# loads files from the following directory '../Resources/Cleaned'
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
