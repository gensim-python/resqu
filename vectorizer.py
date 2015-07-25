from gensim import corpora, models, similarities
documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]
# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
        for token in text:
         frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1] for text in texts]

from pprint import pprint   # pretty-printer
pprint(texts)
dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference
print(dictionary)	
print(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
print(corpus)
dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
print(dictionary)
from gensim import corpora
# create a toy corpus of 2 documents, as a plain Python list
corpus = [[(1, 0.5)], []]  # make one document empty, for the heck of it
corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)

from gensim import corpora
corpus = [[(1, 0.5)], []]  # make one document empty, for the heck of it
corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)
corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm')
print(corpus)

tfidf = models.TfidfModel(corpus)
doc_bow = [(0, 1), (1, 1)]
print(tfidf[doc_bow])

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
     print(doc)

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
lsi.print_topics(2)


