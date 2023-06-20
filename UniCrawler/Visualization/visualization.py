

from gensim import corpora
from gensim.models import LdaModel, ldamodel
from gensim.utils import simple_preprocess
import re, numpy as np, pandas as pd
from pprint import pprint

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

                # initialize dataframe for output
                sent_topics_df = pd.DataFrame()

                # Get main topic in each document
                for i, row_list in enumerate(lda_model[corpus]):
                    row = row_list[0] if lda_model.per_word_topics else row_list
                    # print(row)
                    row = sorted(row, key=lambda x: (x[1]), reverse=True)
                    # Get the Dominant topic, Perc Contribution and Keywords for each document
                    for j, (topic_num, prop_topic) in enumerate(row):
                        if j == 0:  # => dominant topic
                            wp = lda_model.show_topic(topic_num)
                            topic_keywords = ", ".join([word for word, prop in wp])
                            sent_topics_df = sent_topics_df._append(
                                pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]), ignore_index=True)
                        else:
                            break
                sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

                # Add original text to the end of the output
                contents = pd.Series(processed_texts)
                sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)

                df_topic_sents_keywords = sent_topics_df

                # Format
                df_dominant_topic = df_topic_sents_keywords.reset_index()
                df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
                df_dominant_topic.head(10)

                pprint(df_dominant_topic)

                # helpDict['stud_url'] = i['stud_url']
                # helpDict['title'] = i['title']
                # helpDict['paragraphs'] = tokens
                #
                # content.append(helpDict)

            else:
                print(f"Element is not a dict: {type(i)}")
    else:
        print(f"{fname} is not a valid JSON file.")


    if df_dominant_topic is not None:
        write_txt("../Visualization/" + os.path.basename(fname).split("_")[0], df_dominant_topic)
    else:
        print(f"Content is empty, something went wrong with: {fname}")


# writes a new JSON file for every processed document
def write_txt(fname, df):
    df.to_csv(fname + "_vis.csv", index=False)
    df.to_excel(fname + "_vis.xlsx", index=False)

# fname = "../Resources/Cleaned/hawoutput_cleaned.json"
# apply_lda(fname)

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
