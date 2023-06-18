# Python program to READ and CLEAN
# JSON file - creates a new file to keep raw data

import json
import os
import re
import spacy

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# # einmaliges Ausführen
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')

# vorher via Konsole: spacy download de_core_news_sm
# Laden deutschen Sprachmodells von Spacy
nlp = spacy.load("de_core_news_sm")

stopList = "additional_words.json"

def clean_string(input):
    if input is not None:
        input = input.strip()
        text = re.sub(r'[^\w\s]|[\d]', '', str(input))
        lowercase_tokens = [token.lower() for token in word_tokenize(text, language='german')]
        return lowercase_tokens
    else:
        return ''


def clean_json(fname):
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
                    # List comprehension wär vielleicht schöner also das e.strip but what do I know
                    # .strip() um whitespace zu entfernen
                    helpList.append(e.strip())

                # RegEX das weiter aufräumt
                text = re.sub(r'[^\w\s]|[\d]', '', str(helpList))
                # print(text)

                # trainiertes nltk wordtokenize, macht aus Sätzen Wörter und mit schreibt sie klein
                lowercase_tokens = [token.lower() for token in word_tokenize(text, language='german')]

                # clear title
                something = clean_string(i['title'])
                # print(f"Clean title: {something}")

                # StopWords sind Füllwörter
                stop_words = set(stopwords.words("german"))
                additional_words = list()

                # Liste mit weiteren Wörtern die rausgefiltert werden

                with open(stopList) as f:
                    additional_words = json.load(f)
                    #print(additional_words)

                stop_words.update(additional_words)

                # legt neue Liste an mit gefilterten Wörtern
                try:
                    filtered_tokens = [token for token in lowercase_tokens if token not in stop_words]
                    # print(f"FILTERED {filtered_tokens}")
                except Exception as e:
                    print(f"Fehlermeldung: {e}")

                combined_string = ' '.join(filtered_tokens)
                doc = nlp(combined_string)
                # print(combined_string)

                # entferne Adverben, Determinante, ADP und Pronomen
                removable_tags = ['ADV', 'DET', 'ADP', 'PRON']
                filtered_token = [token.text for token in doc if token.pos_ not in removable_tags]
                # print(filtered_token)

                filtered_string = ' '.join(filtered_tokens)
                filtered_doc = nlp(filtered_string)

                tokens = list()
                for chunk in filtered_doc.noun_chunks:
                    tokens.append(chunk.text)

                tokens.append(' '.join(something))
                # print(tokens)

                helpDict['stud_url'] = i['stud_url']
                helpDict['title'] = i['title']
                helpDict['paragraphs'] = tokens

                content.append(helpDict)

            else:
                print(f"Listenelement ist kein Dict: {type(i)}")
    else:
        print(f"{fname} ist keine gültige JSON.")

    if content is not None:
        write_json("../Resources/Cleaned/" + os.path.basename(fname).split(".")[0] + "_cleaned.json",  content)
    else:
        print(f"Content is empty, something went wrong with: {fname}")


def write_json(fname, content):
    with open(fname, 'w') as f:
        json.dump(content, f)
        print(f"JSON Datei {fname} erfolgreich erstellt")


# theoretisch als funktion

for root, dirs, files in os.walk('../Resources'):
    if root == "../Resources":
        for file in files:
            # check for json file
            if (file.endswith('.json')):
                fname = root + '/' + file
                clean_json(fname)
            else:
                print(f"{file} has no json extension.")
    print("finished, no more json files")
