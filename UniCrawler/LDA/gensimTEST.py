from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess

import os
import json


def apply_lda(fname):
    content = list()
    # open file
    try:
        with open(fname) as f:
            data = json.load(f)

    except Exception as e:
        print(f"when opening {fname} an error occurred")
        print(f"Error: {e}")

    # check json format
    if type(data) is list:
        print(f"{fname} is in the correct format")

        for i in data:
            # if type(i) is dict:
            if isinstance(i, dict):
                helpList = list()
                helpDict = dict()
                for e in i['paragraphs']:
                    helpList.append(e)
                texts = helpList

                # tokenization and further processing of text
                processed_texts = [simple_preprocess(text) for text in texts]
                dictionary = corpora.Dictionary(processed_texts)
                corpus = [dictionary.doc2bow(text) for text in processed_texts]

                # training LDA-model
                # iterates 10 times over a text to 'learn' it
                num_topics = 5
                lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=10)

                # output
                tokens = list()
                topics = lda_model.print_topics(num_words=5)
                for topic in topics:
                    tokens.append(topic[1])

                helpDict['stud_url'] = i['stud_url']
                helpDict['title'] = i['title']
                helpDict['paragraphs'] = tokens

                content.append(helpDict)

            else:
                print(f"Element is not a dict: {type(i)}")
    else:
        print(f"{fname} is not a valid JSON file.")

    if content is not None:
        write_json("../LDA/GensimOutput/" + os.path.basename(fname).split("_")[0] + "_gensim.json", content)
    else:
        print(f"Content is empty, something went wrong with: {fname}")


# writes a new JSON file for every processed document
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
