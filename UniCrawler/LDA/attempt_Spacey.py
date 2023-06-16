import spacy

from spacy.lang.de import German
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

## whatevery ey sauberer code sieht anders aus aber .. fürn Garten reichts

# Laden deutschen Sprachmodells von Spacy (oder so ähnlich)
nlp = spacy.load("de_core_news_sm")

# die Inhalte kommen aus der Konsolenausgabe der cleanJSON.py in der ich mir die getokenized Wörter mit der immer wieder angepassten Stopword Liste habe ausgeben lassen um so Stück für Stück weitere Stopwords zu identifizieren
# Maschinenbau
text = ['bachelor', 'vollzeit', 'teilzeit', 'wintersemester', 'bildung', 'fachlichen', 'erforderlichen', 'kenntnisse',
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
# ['bachelor', 'vollzeit', 'wintersemester', 'bildung', 'fachlichen', 'erforderlichen', 'kenntnisse', 'wintersemester', 'instruktionen', 'wesentlichexakenntnisse', 'kernfächern', 'agrarwirtschaft', 'xaökonomie', 'tierproduktion', 'pflanzenproduktion', 'landtechnik', 'betriebswirtschaft', 'kenntnisse', 'anwendungsorientiert', 'vermittelt', 'ermöglichenxaihnen', 'landwirtschaftlichen', 'betrieb', 'entscheidungenxain', 'produktionstechnik', 'verfahrensabläufen', 'betriebswirtschaft', 'vorzubereiten', 'treffen', 'außerdem', 'befähigt', 'betriebe', 'verfahren', 'zuxaplanen', 'bewerten', 'besonders', 'wichtig', 'dasxaerkennen', 'analyse', 'schnittstellen', 'zwischenxaden', 'wissensgebieten', 'deshalb', 'ihrxaproduktionstechnisches', 'wissen', 'ökonomischen', 'rahmenbedingungen', 'betriebswirtschaftlichen', 'methodenxader', 'entscheidungsfindung', 'verknüpfen', 'ausbildungsziele', 'lernen', 'alltag', 'landwirtschaftlichen', 'betriebes', 'gehört', 'bieten', 'campus', 'pillnitz', 'mitten', 'grünen', 'praxiserfahrung', 'lehrenden', 'ideale', 'vermittelten', 'vielfältigen', 'wissen', 'unterschiedlichsten', 'wege', 'berufsleben', 'offen', 'praxisorientiertes', 'grundlagenwissen', 'kerngebieten', 'agrarwirtschaft', 'drei', 'pflichtmodule', 'anschließendem', 'wöchigen', 'praktikum', 'anerkannten', 'ausbildungsbetrieb', 'anwendungsorientierte', 'fachkenntnisse', 'pflicht', 'wahlpflichtmodulen', 'planungsprojekte', 'wöchige', 'abschlussarbeit', 'präsenzmodule', 'rahmen', 'projektes', 'rwerb', 'erufsabschlusses', 'achelor', 'grarwirtschaft', 'landwirtin', 'erworben', 'praxisnähe', 'leitung', 'landw', 'handel', 'vertrieb', 'landw', 'produktionsmittel', 'beratung', 'landw', 'tätigkeit', 'landw', 'versuchswesen', 'statt', 'vereinbarung', 'internationale', 'studienberatung', 'vereinbarung', 'dresden']

# habe hier die Tokenisierung geskipped weil Text kommt ja aus unserer clean Datei .. außerdem - da sind die Stopwords drin in der cleanJSON

# Vektorisierung des Text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

# Training LDA-Modell
num_topics = 5
lda_model = LatentDirichletAllocation(n_components=num_topics)
lda_model.fit(X)

# Themen ausgeben
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda_model.components_):
    top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
    print(f"Topic #{topic_idx + 1}: {', '.join(top_words)}")

    print(("I'M DONE"))
