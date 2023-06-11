# Python program to READ and CLEAN
# JSON file

import json
import re

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
                helpList.append(e.strip())
            text = re.sub(r'[^\w\s]|[\d]', '', str(helpList))

# hier weiter aufräumen

            helpDict['stud_url'] = i['stud_url']
            helpDict['title'] = i['title']
            helpDict['paragraphs'] = text

            content.append(helpDict)

        else:
            print("Listenelemet ist kein Dict")
else:
    print(f"{fname} ist keine Liste.")

with open(outputFile, 'w') as f:
    json.dump(content, f)
