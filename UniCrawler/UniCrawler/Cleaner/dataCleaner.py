import json

filepath = "../haw.json"
cleanData = list()

try:
    with open(filepath, 'r',  encoding="utf8") as file:
        dataFile = json.load(file)
except Exception as e:
    print("An error occurred while reading the file:", str(e))

for course in dataFile:
    print(course['paragraphs'])


with open("hawClean.json", "w") as outfile:
    json.dump(cleanData, outfile)