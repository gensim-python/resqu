from gensim import corpora, models, similarities
from time import time
import os

BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
# print os.path.abspath(BASEDIR)
DATADIR = os.path.join(os.path.abspath(BASEDIR), "data")
# print DATADIR


# Step 1
#Loading the existing dictionary
dictionary = corpora.Dictionary.load("abstracts_without_GS.dict")
# #add the gold standard tokens to the existing corpus dictionary
GSDATADIR = os.path.join(DATADIR,"abstracts_with_GS_rawText.txt")
for line in open(GSDATADIR, "r"):
    splitLine = line.strip().split('|')

text = [];
for i in range(len(splitLine)):
    print  splitLine[i], "\n"
    text.insert(splitLine[i])
    dictionary.add_documents(list(text))

# Step 2
# corpus = list() #list of list each list is a bag of words for a document
# for concept in summary:
# 	pmids = get_pmids_for_concept(concept)
# 	concept_context = list()
# 	for pmid in pmids:
# 		context = get_text_as_list(pmid)
# 		concept_context.append(context)
# 	#convert the list of concept token to bag of words using the dictionary
# 	concept_bow = dictionary.doc2bow(concept_context)
#
# 	#add the bag of words for the concept to the corpus
# 	corpus.append(concept_bow)
#
# #generate the tfidf model from the corpus (list of lists)
# tfidf = TfidfModel(corpus)


# Step 2