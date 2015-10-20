import logging
import os
from gensim import corpora, models, similarities

#Base directory path
path="/home/nishita/resqu/data/documentCorpus/"

#Reading each fiel in the directory
for file in os.listdir("/home/nishita/resqu/data/documentCorpus/"):
    #Stop word list 
    stoplist = set('for a of the and to in'.split())
    #Re-construct file name for reading
    filepath = os.path.join(path, file)
    #Dictionary creation using gensim library
    dictionary = corpora.Dictionary(line.lower().split() for line in open(filepath,"r"))
    #stop-words from dictionary
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
    #words that occuring only once
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    
    dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
    dictionary.compactify() # remove gaps in id sequence after words that were removed

#Serializing the dictionay to .dict file   
dictionary.save('abstract.dict')

texts = [[word for word in line.lower().split() if word not in stoplist] for line in open(filepath)]
corpus = [dictionary.doc2bow(line) for line in texts]
#Serializing corpus to ,mm file
corpora.MmCorpus.serialize('abstract.mm', corpus)
