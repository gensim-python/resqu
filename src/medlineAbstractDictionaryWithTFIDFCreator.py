#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

This script just show the basic workflow to compute TF-IDF similarity matrix with Gensim


OUTPUT :

clemsos@miner $ python gensim_workflow.py


How to use Gensim to compute TF-IDF similarity step by step
----------
Let's start with a raw corpus :<type 'list'>

STEP 1 : Index and vectorize
----------
We create a dictionary, an index of all unique values: <class 'gensim.corpora.dictionary.Dictionary'>
Then convert convert tokenized documents to vectors: <type 'list'>
Save the vectorized corpus as a .mm file

STEP 2 : Transform and compute similarity between corpuses
----------
We load our dictionary : <class 'gensim.corpora.dictionary.Dictionary'>
We load our vector corpus : <class 'gensim.corpora.mmcorpus.MmCorpus'>
We initialize our TF-IDF transformation tool : <class 'gensim.models.tfidfmodel.TfidfModel'>
We convert our vectors corpus to TF-IDF space : <class 'gensim.interfaces.TransformedCorpus'>

STEP 3 : Create similarity matrix of all files
----------
We compute similarities from the TF-IDF corpus : <class 'gensim.similarities.docsim.MatrixSimilarity'>
We get a similarity matrix for all documents in the corpus <type 'numpy.ndarray'>

Done in 0.011s

'''
from gensim import corpora, models, similarities
from time import time
import os

t0=time()

# keywords have been extracted and stopwords removed.
#Base directory path
BASEDIR_TEST=os.path.dirname(__file__)
BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)

#Reading each fiel in the directory
document_corpus = os.path.join(BASEDIR, 'data', 'documentCorpus')
for file in os.listdir(document_corpus):
    #Re-construct file name for reading
    filepath = os.path.join(document_corpus, file)


print "How to use Gensim to compute TF-IDF similarity step by step"
print '-'*10
print "Let's start with a raw corpus :%s"%type(document_corpus)
print
# STEP 1 : Compile corpus and dictionary
print "STEP 1 : Index and vectorize"
print '-'*10

# create dictionary (index of each element)

#Dictionary creation using gensim library
dictionary = corpora.Dictionary(line.lower().split() for line in open(filepath,"r"))
#words that occuring only once
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
# remove stop words and words that appear only once
dictionary.filter_tokens(once_ids)
dictionary.save('abstract_with_GS.dict') # store the dictionary, for future reference
print "Create a dictionary, an index of all unique values: %s"%type(dictionary)

# compile corpus (vectors number of times each elements appears)
texts = [[word for word in pmid_docs.lower().split()] for pmid_docs in open(filepath)]
raw_corpus = [dictionary.doc2bow(pmid_docs) for pmid_docs in texts]
#Serializing corpus to .mm file
print "Converting tokenized documents to vectors: %s"% type(raw_corpus)
corpora.MmCorpus.serialize('abstract_with_GS.mm', raw_corpus) # store to disk
print "Saving the vectorized corpus as a .mm file"
print

# STEP 2 : similarity between corpuses
print "STEP 2 : Transform and compute similarity between corpuses"
print '-'*10
dictionary = corpora.Dictionary.load('abstract_with_GS.dict')
print "Load the dictionary : %s"% type(dictionary)

corpus = corpora.MmCorpus('abstract_with_GS.mm')
print "Load the vector corpus : %s "% type(corpus)

# Transform Text with TF-IDF
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
print "Initialize the TF-IDF transformation tool : %s"%type(tfidf)

# corpus tf-idf
corpus_tfidf = tfidf[corpus]
print "Converting vectors corpus to TF-IDF space : %s"%type(corpus_tfidf)
print

# STEP 3 : Create similarity matrix of all files
print "STEP 3 : Creating similarity matrix of all files"
print '-'*10
index = similarities.MatrixSimilarity(tfidf[corpus])
print "Computing similarities from the TF-IDF corpus : %s"%type(index)
index.save('abstract_with_GS.index')
index = similarities.MatrixSimilarity.load('abstract_with_GS.index')

sims = index[corpus_tfidf]
print "Get a similarity matrix for all documents in the corpus %s"% type(sims)
print
print "Done in %.3fs"%(time()-t0)

print sims
print list(enumerate(sims))
sims = sorted(enumerate(sims), key=lambda item: item[1])
# print sims
# print sorted (document number, similarity score) 2-tuples