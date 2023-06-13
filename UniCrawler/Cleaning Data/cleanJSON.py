# Python program to READ and CLEAN
# JSON file - creates a new file to keep raw data

import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import *

# open JSON file
fname = "../htwoutput.json"
content = list()
outputFile = "htw_clean.json"

try:
    with open(fname) as f:
        data = json.load(f)

except Exception as e:
    print(f"beim Öffnen von {fname} ist ein Fehler aufgetreten")
    print(f"Fehlermeldung: {e}")

# prüfen ob eingegebene Datei eine Liste ist
if type(data) is list:
    print(f"{fname} entspricht dem richtigen Typ")

    for i in data:
        if type(i) is dict:
            helpList = list()
            helpDict = dict()
            for e in i['paragraphs']:
                # List comprehension wär vielleicht schöner also das e.strip but what do I know
                # .strip() um whitespace zu entfernen
                helpList.append(e.strip())

            # RegEX das weiter aufräumt
            text = re.sub(r'[^\w\s]|[\d]', '', str(helpList))
            #print(text)

            # # einmaliges Ausführen
            # nltk.download('punkt')
            # nltk.download('stopwords')
            # nltk.download('wordnet')
            # nltk.download('omw-1.4')
            # nltk.download('averaged_perceptron_tagger')

            # trainiertes nltk wordtokenize, macht aus Sätzen Wörter und mit schreibt sie klein
            lowercase_tokens = [token.lower() for token in word_tokenize(text, language='german')]

            # StopWords sind Füllwörter
            stop_words = set(stopwords.words("german"))

            # Liste mit weiteren Wörtern die rausgefiltert werden
            additional_words = ['innen', 'bitte', 'xa', 'prof', 'pdf', 'z', 'b', 'haw', 'oft', 'per', 'sowie', 'etc',
                                'uhr', 'ab', 'mo', 'di', 'mi', 'do', 'fr', 'sa', 'so', 'aktivieren', 'javascript',
                                'browser', 'og', 'angebotenxaneben', 'google', 'deutsch', 'deutsche', 'deutscher',
                                'deutschen', 'schule', 'unserer', 'homepage', 'ausland', 'ausländische', 'ausländischer', 'hzb',
                                'zumxabewerbungsverfahren', 'frist',
                                'or', 'a', 'of', 'about', 'the', 'on', 'our', ]
            stop_words.update(additional_words)

            # legt neue Liste an mit gefilterten Wörtern
            try:
                filtered_tokens = [token for token in lowercase_tokens if token not in stop_words]
                #print(f"FILTERED {filtered_tokens}")
            except Exception as e:
                print(f"Fehlermeldung: {e}")

            # reduziert Worte auf deutsche Wortstämme
            stemmer = SnowballStemmer("german")
            stemmed_words = []

            for w in filtered_tokens:
                stemmed_words.append(stemmer.stem(w))
            #print(f"STEMMED {stemmed_words}")

            # ab her eventuell weitere Reinigung vornehmen

            helpDict['stud_url'] = i['stud_url']
            helpDict['title'] = i['title']
            helpDict['paragraphs'] = stemmed_words

            content.append(helpDict)

        else:
            print("Listenelemet ist kein Dict")
else:
    print(f"{fname} ist keine Liste.")

with open(outputFile, 'w') as f:
    json.dump(content, f)
    print(f"JSON Datei {outputFile} erfolgreich erstellt")
