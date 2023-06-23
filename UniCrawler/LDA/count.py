import os
import json

'''
Note: nicht alle davon sind Studiengänge. Teils sind's auch organisatorische sachen
Number of entries of ../Resources/Cleaned/fhwoutput_cleaned.json:  15
Number of entries of ../Resources/Cleaned/htwkoutput_cleaned.json:  773
Number of entries of ../Resources/Cleaned/htwoutput_cleaned.json:  48
Number of entries of ../Resources/Cleaned/tuberlinoutput_cleaned.json:  152
Number of entries of ../Resources/Cleaned/uloutput_cleaned.json:  1713


Folgende Feststellungen:
in htwkoutput sind Mehrfachnennungen drin, f.e. Buch- und Medienproduktion gibt's 20 mal
mit unterschiedlichen Links.  Elektrotechnik und Informationstechnik 
gibt es 39 mal (teilweise noch mit kooperativ hintendran)
Außerdem sind Organisatorische Inhalte in den Daten drin

Uni Lübeck einfach absolut wild. Sehr viele unnötige Daten drin, die eigtl im Vorfeld
noch Sortiert werden mssten aber wir nicht zu gekommen sind. 

'''

def count(fname):
    try:
        with open(fname) as f:
                data = json.load(f)
        # Count the entries
        num_entries = len(data)
        print(f"Number of entries of {fname} ", num_entries)

    except Exception as e:
        print(f"beim Öffnen von {fname} ist ein Fehler aufgetreten")
        print(f"Fehlermeldung: {e}")



for root, dirs, files in os.walk('../Resources/Cleaned'):
    if root == "../Resources/Cleaned":
        for file in files:
        # check for json file
            if (file.endswith('.json')):
                fname = root + '/' + file
                count(fname)
        print("finished, no more json files")
