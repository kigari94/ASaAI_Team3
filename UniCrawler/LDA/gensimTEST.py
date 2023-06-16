from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess

## ist noch 100% kein fertiges Programm aber ich wollte bloß gucken ob es geht aber ich werd da wohl noch was schreiben


# die Inhalte kommen aus der Konsolenausgabe der cleanJSON.py in der ich mir die getokenized Wörter mit der immer wieder angepassten Stopword Liste habe ausgeben lassen um so Stück für Stück weitere Stopwords zu identifizieren
# Maschinenbau glaube
texts = ['bachelor', 'vollzeit', 'teilzeit', 'wintersemester', 'bildung', 'fachlichen', 'erforderlichen', 'kenntnisse',
         'wintersemester', 'instruktionen', 'absolventin', 'maschinenbaus', 'breit', 'gefächertes', 'grundlagenwissen',
         'praxisorientierte', 'fertigkeiten', 'tätigkeiten', 'bereichen', 'maschinenwesens', 'qualifiziert', 'darüber',
         'hinaus', 'gutachterwesen', 'eingesetzt', 'fachkenntnisse', 'werkstoffe', 'einzelne', 'bauteile', 'deren',
         'hochkomplexen', 'maschinensystemen', 'zudem', 'kennen', 'verschiedenste', 'herstellungsverfahren',
         'wirkzusammenhänge', 'steuerungs', 'messtechniken', 'lage', 'technische', 'problemlösungen', 'befähigt',
         'entwicklung', 'berechnung', 'auslegung', 'konstruktion', 'maschinen', 'technischen', 'anlagen',
         'maschinenbaustudium', 'bildet', 'grundlage', 'viele', 'herausforderungen', 'hineinzudenken', 'lösungswege',
         'aufzubauen', 'umfassend', 'vorbereitet', 'generalistisches', 'wissen', 'unterschiedlichste',
         'tätigkeitsgebiete', 'grundlagenwissen', 'mathematik', 'physik', 'werkstofftechnik', 'studienkompetenzen',
         'vertiefendes', 'fachwissen', 'wahl', 'studienrichtung', 'konstruktion', 'fahrzeugtechnik', 'nachhaltige',
         'fertigung', 'management', 'wöchiges', 'betriebspraktikum', 'abschlussarbeit', 'statt', 'internationale',
         'studienberatung', 'vereinbarung', 'dresden']

# Agrarsonstwas
#  ['bachelor', 'vollzeit', 'wintersemester', 'bildung', 'fachlichen', 'erforderlichen', 'kenntnisse', 'wintersemester', 'instruktionen', 'wesentlichexakenntnisse', 'kernfächern', 'agrarwirtschaft', 'xaökonomie', 'tierproduktion', 'pflanzenproduktion', 'landtechnik', 'betriebswirtschaft', 'kenntnisse', 'anwendungsorientiert', 'vermittelt', 'ermöglichenxaihnen', 'landwirtschaftlichen', 'betrieb', 'entscheidungenxain', 'produktionstechnik', 'verfahrensabläufen', 'betriebswirtschaft', 'vorzubereiten', 'treffen', 'außerdem', 'befähigt', 'betriebe', 'verfahren', 'zuxaplanen', 'bewerten', 'besonders', 'wichtig', 'dasxaerkennen', 'analyse', 'schnittstellen', 'zwischenxaden', 'wissensgebieten', 'deshalb', 'ihrxaproduktionstechnisches', 'wissen', 'ökonomischen', 'rahmenbedingungen', 'betriebswirtschaftlichen', 'methodenxader', 'entscheidungsfindung', 'verknüpfen', 'ausbildungsziele', 'lernen', 'alltag', 'landwirtschaftlichen', 'betriebes', 'gehört', 'bieten', 'campus', 'pillnitz', 'mitten', 'grünen', 'praxiserfahrung', 'lehrenden', 'ideale', 'vermittelten', 'vielfältigen', 'wissen', 'unterschiedlichsten', 'wege', 'berufsleben', 'offen', 'praxisorientiertes', 'grundlagenwissen', 'kerngebieten', 'agrarwirtschaft', 'drei', 'pflichtmodule', 'anschließendem', 'wöchigen', 'praktikum', 'anerkannten', 'ausbildungsbetrieb', 'anwendungsorientierte', 'fachkenntnisse', 'pflicht', 'wahlpflichtmodulen', 'planungsprojekte', 'wöchige', 'abschlussarbeit', 'präsenzmodule', 'rahmen', 'projektes', 'rwerb', 'erufsabschlusses', 'achelor', 'grarwirtschaft', 'landwirtin', 'erworben', 'praxisnähe', 'leitung', 'landw', 'handel', 'vertrieb', 'landw', 'produktionsmittel', 'beratung', 'landw', 'tätigkeit', 'landw', 'versuchswesen', 'statt', 'vereinbarung', 'internationale', 'studienberatung', 'vereinbarung', 'dresden']

# Tokenisierung und Vorbereitung vom Text
processed_texts = [simple_preprocess(text) for text in texts]
dictionary = corpora.Dictionary(processed_texts)
corpus = [dictionary.doc2bow(text) for text in processed_texts]

# Training des LDA-Modells
# Anzahl topics = 5 passes=10 also es ghet 10 Mal über die Daten drüber um sie zu erlernen (wenn ich das richtig verstanden habe)
num_topics = 5
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=10)

# Ausgabe
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)
