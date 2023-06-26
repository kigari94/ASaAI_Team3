# Web Scraping and Data Analysis
This repository is containing an university related python project for the course adaptive systems and artificial intelligence.

Goal of the project is to collect data from certain university websites all over germany to analyse and categories their different courses by using a combination of Scrapy, NLP, SciKit and LDA.
In the end the analysis shall give an overview about the different topics and how they are distributed.

The project structure contains different folders for each step of the process. The process is starting by retrieving the required data via Scrapy. For those purpose there are different spiders located in the UniCrawler folder. Running them will give rough sets of data stored in a JSON file.

The second step is about cleaning and transforming the data which can be done by running the cleanJSON.py inside the cleaning data folder. In the very same folder is also a file located, named additional_words.json, for adjusting the stopwords which will filter non required data.

The last step can be found inside the LDA folder where we have different scripts for the topic recognition. Running the scikit_LDA.py will get the most occuring words for each course.

Note: As this project is a prototype only, there still might be contradictions regarding the scraped and processed datas.
