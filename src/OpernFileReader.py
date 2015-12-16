from gensim import corpora, models, similarities
from time import time
import os
import os.path


BASEDIR = os.path.join(os.path.dirname(__file__),os.path.pardir)
# print "hello: ",BASEDIR
DATADIR = os.path.join(BASEDIR, "data")
# DATADIR_INP = os.path.join(BASEDIR, 'data', 'input')

DATADIR_INP= "/home/nishita/resqu/data/input/disease/"
DICTDIR = "/home/nishita/resqu/data/abstracts_without_GS.dict"
dictionary = corpora.Dictionary.load(DICTDIR)

# print "datadir : ", DATADIR_INP


for file in os.listdir(DATADIR_INP):
        #Re-construct file name for reading
        filepath = os.path.join(DATADIR, file)
        # print "file : ", filepath
        if os.path.isdir(os.path.join(DATADIR_INP,file)) == True:
            # print "it is a dir : ", os.path.join(DATADIR_INP,file)
            for inner_file in os.listdir(os.path.join(DATADIR_INP,file)):
                if(inner_file.endswith("ABS")):
                    filepath_inner = os.path.join(os.path.join(DATADIR_INP,file),inner_file)
                    print "inner_file : ",filepath_inner
                    corpus = list() #list of list each list is a bag of words for a document
                    for line in open(filepath_inner,"rb"):
                        context_corpus =list()
                        # print line
                        # if line.startswith("AB  - "):
                            # print "AB : ",line
                        context_corpus.append(line.replace("AB  - ",""))
                        # result= ''.join(context_corpus)
                        print context_corpus
                        #convert the list of concept token to bag of words using the dictionary
                        concept_bow = dictionary.doc2bow(context_corpus)

                        #add the bag of words for the concept to the corpus
                        corpus.append(concept_bow)

                    #generate the tfidf model from the corpus (list of lists)
                    tfidf = models.TfidfModel(corpus)
                    corpus_tfidf = tfidf[corpus]
                    tfidf = models.TfidfModel(corpus_tfidf, id2word=dictionary)
                    tfidf.save('data/abstract_without_GS_TestPipeline.tfidf')





