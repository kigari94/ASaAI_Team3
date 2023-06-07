import nltk
import re
import os
import json

'''
Packages:
* nltk 
Im Deutschen gibt's für die Lemmatisierung und Wortartenerkennung (POS Tagger) bspw. den Hanover Tagger Doku: https://github.com/wartaal/HanTa/blob/master/Demo.ipynb
* pip install --upgrade HanTa 

Weitere Dependencies: 
numpy, scipy, gensim (bisher net genutzt), matplotlib, 

-> einmal ausführen damit ihr den Bums habt
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
'''


'''
Laden des json Files. Zukünftig müssen wir aber unbedingt nur die Spalten mit den Infos ansprechen,
sonst sind die URLs und alles andere Weg, was zur Idenfitikation wichtig sein könnte.
Mit dem Encoding wirft er auch keinen Fehler weil irgendein Deutsches Zeichen ihn rausschmeißt.
'''
try:
    with open('test.json', 'r',  encoding="utf8") as file:
        data = json.load(file)
except Exception as e:
    print("An error occurred while reading the file:", str(e))

'''
ReGeX um die div tags, sonderzeichen usw rauszufiltern. Fehlt noch so \h  und so. 
Bin net so gut im regexen
'''
try:
    text = re.sub(r'<\/?div[^>]*>|[^\w\s]|[\d]', '', str(data))

except Exception as e:
    print("Help me: ", str(e))

'''
trainiertes nltk wordtokenize. Das macht aus all den Sätzen einzelne Wörter und mit
token.lower(), werden die alle kleingemacht, damit im nächsten Step die Stopwörter gut rausgefiltert werden können
sonst würde er n großgeschriebenes Die bspw nicht erkennen.
'''
from nltk.tokenize import word_tokenize

lowercase_tokens = [token.lower() for token in word_tokenize(text, language='german')]

'''
StopWords, sind Füllwörter. Ich hab einfach n paar hinzugefügt und geprinted. 
'''
from nltk.corpus import stopwords
stop_words = set(stopwords.words("german"))
additional_words = ['innen', 'bitte','xa','prof', 'pdf', 'haw','oft','per','sowie', 'etc', 'uhr','ab']
stop_words.update(additional_words)
# komische Wörter wir ubububububububmodi müssen noch raus.. denk das liegt aber an html tags oder \n oder so
try:
    filtered_tokens = [token for token in lowercase_tokens if token not in stop_words]
except Exception as e:
    print("Help me: ", str(e))

#print(filtered_tokens)

'''
snackt sich die Wortstämme auf Deutsch, möglich dass wir damit gut mit language Models
rumspielen können
'''
from nltk.stem import *
stemmer = SnowballStemmer("german")

stemmed_words = []

for w in filtered_tokens:
  stemmed_words.append(stemmer.stem(w))

#print("stemmed Sentence: ", stemmed_words)

'''
POS Tagging -> Wortarterkennung. Ich schätz das ist smart für uns
Wir müssen nochmal checken ob unsere beschreibenden Wörter eher Nomen sind, denn dann kann man
solche Language Models wie TextRank das mitgeben, dass darauf besonderen Wert
gelegt werden soll
Erstmal auskommentiert, weil frisst n bisschen Zeit
'''
from HanTa import HanoverTagger as ht
tagger = ht.HanoverTagger('morphmodel_ger.pgz')

try:
    print("I'm busy")
    #tagged_tokens = [tagger.analyze(token) for token in stemmed_words]
    #print(tagged_tokens)

except Exception as e:
    print("Help me with Tagging: ", str(e))

'''
Frequency check 
Zeigt ganz schön, dass wir mit den häufigsten Wörtern net hinkommen. 
'''
from nltk.probability import FreqDist
frequency = FreqDist(filtered_tokens)
print(frequency, frequency.most_common(30))


import matplotlib.pyplot as plt
frequency.plot(30, cumulative=False)
plt.show()

