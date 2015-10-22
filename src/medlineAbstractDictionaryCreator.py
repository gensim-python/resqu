import os
from collections import defaultdict
from gensim import corpora, models


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

#Adding new code for creating tf-idf model
# documents = []
#
# for file in os.listdir("/home/nishita/resqu/data/documentCorpus/"):
#     f = open(filepath,"r")
#     for line in f:
#             documents.append(line)
#
# texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
#
# # remove words that appear only once
# frequency = defaultdict(int)
# for text in texts:
#         for token in text:
#          frequency[token] += 1
# texts = [[token for token in text if frequency[token] > 0] for text in texts]

# corpus = [dictionary.doc2bow(text) for text in texts]
# corpora.MmCorpus.serialize('abstractCorpus.mm', corpus) # store to disk, for later use

# corpora.BleiCorpus.serialize('/tmp/abstractCorpus.lda-c', corpus)
# dictionary = corpora.Dictionary.load('/tmp/abstractCorpus.dict')
# corpus = corpora.MmCorpus('/tmp/abstractCorpus.mm')
# print(corpus)

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
     print(doc)

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) # initialize an LSI transformation

tfidf = models.TfidfModel(corpus_tfidf, id2word=dictionary)

corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
lsi.print_topics(2)

lsi.save('abstractCorpusModel.lsi') # same for tfidf, lda, ...
lsi = models.LsiModel.load('abstractCorpusModel.lsi')

tfidf.save('abstractCorpusModel.tfidf') # same for tfidf, lda, ...
tfidf = models.LsiModel.load('abstractCorpusModel.tfidf')


