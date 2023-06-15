import json

import gensim
from nltk import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import *
from nltk.stem.porter import *



fname = "../hawoutput.json"
content = list()
outputFile = "haw_lda.json"
results = []

try:
    with open(fname, encoding="utf8") as f:
        data = json.load(f)
        print("loading JSON succeeded")

except Exception as e:
    print(f"beim Öffnen von {fname} ist ein Fehler aufgetreten")
    print(f"Fehlermeldung: {e}")


def lemmatize_stemming(text):
    stemmer = SnowballStemmer("german")
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


if type(data) is list:
    print(f"{fname} entspricht dem richtigen Typ")

    for i in data:
        if type(i) is dict:
            helpList = list()
            helpDict = dict()
            for e in i['paragraphs']:
                # Tokenize and lemmatize

                for token in gensim.utils.simple_preprocess(e):
                    if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                        # print(lemmatize_stemming(token))
                        results.append(lemmatize_stemming(token))
                        # print(results)

            # print("Test")
            print(results)
            dataset = [r.split() for r in results]
            dictionary = gensim.corpora.Dictionary(dataset)

            bow_corpus = [dictionary.doc2bow(d) for d in dataset]

            lda_model = gensim.models.LdaMulticore(bow_corpus,
                                                   num_topics=8,
                                                   id2word=dictionary,
                                                   passes=10,
                                                   workers=2)
            print(lda_model)

            helpDict['stud_url'] = i['stud_url']
            helpDict['title'] = i['title']
            helpDict['paragraphs'] = results

            content.append(helpDict)

        else:
            print("Listenelemet ist kein Dict")
else:
    print(f"{fname} ist keine Liste.")

with open(outputFile, 'w') as f:
    json.dump(content, f)
    print(f"JSON Datei {outputFile} erfolgreich erstellt")
