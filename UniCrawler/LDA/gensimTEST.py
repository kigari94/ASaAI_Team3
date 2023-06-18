from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess
import json
import re
import spacy

import os
import json


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
                texts = helpList
                # print(text)

                # Tokenisierung und Vorbereitung vom Text
                processed_texts = [simple_preprocess(text) for text in texts]
                dictionary = corpora.Dictionary(processed_texts)
                corpus = [dictionary.doc2bow(text) for text in processed_texts]

                # Training des LDA-Modells
                # Anzahl topics = 5 passes=10 also es ghet 10 Mal über die Daten drüber um sie zu erlernen
                num_topics = 5
                lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=10)

                # Ausgabe
                tokens = list()
                topics = lda_model.print_topics(num_words=5)
                for topic in topics:
                    #print(topic)
                    tokens.append(topic[1])

                helpDict['stud_url'] = i['stud_url']
                helpDict['title'] = i['title']
                helpDict['paragraphs'] = tokens

                content.append(helpDict)

            else:
                print(f"Listenelement ist kein Dict: {type(i)}")
    else:
        print(f"{fname} ist keine gültige JSON.")

    if content is not None:
        write_json("../LDA/GensimOutput/" + os.path.basename(fname).split("_")[0] + "_gensim.json", content)
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
