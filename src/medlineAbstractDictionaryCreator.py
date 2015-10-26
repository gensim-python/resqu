import os
from collections import defaultdict
from gensim import corpora, models


#Base directory path
BASEDIR_TEST=os.path.dirname(__file__)
BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)

#Reading each fiel in the directory
document_corpus = os.path.join(BASEDIR, 'data', 'documentCorpus')
for file in os.listdir(document_corpus):
    #Re-construct file name for reading
    filepath = os.path.join(document_corpus, file)
    #Dictionary creation using gensim library
    dictionary = corpora.Dictionary(line.lower().split() for line in open(filepath,"r"))
    #words that occuring only once
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    # remove stop words and words that appear only once
    dictionary.filter_tokens(once_ids)

#Serializing the dictionay to .dict file
dictionary.save('abstract_without_GS.dict')

texts = [[word for word in pmid_docs.lower().split()] for pmid_docs in open(filepath)]
corpus = [dictionary.doc2bow(pmid_docs) for pmid_docs in texts]
#Serializing corpus to .mm file
corpora.MmCorpus.serialize('abstract_without_GS.mm', corpus)

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
tfidf = models.TfidfModel(corpus_tfidf, id2word=dictionary)
tfidf.save('abstract_without_GS_CorpusModel.tfidf') # same for tfidf, lda, ...
tfidf = models.LsiModel.load('abstract_without_GS_CorpusModel.tfidf')

dictionary.add_documents()


