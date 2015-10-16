from dictionary import DictionaryBuilder
import scipy as sp
import numpy as np

features = []

def get_dict():
    db = DictionaryBuilder() #reads the corpus.txt file by default
    return db.dictionary
    
def create_features(d, corpus_file):
    corpus = []
    with open(corpus_file, "rb") as infile:
        documents = infile.readlines() # convert to bag of words model
        for doc in documents:
            doc_words = [token for token in (doc.lower().split())]
            bow = d.doc2bow(doc_words)
            corpus.append(bow)
    
            print doc.strip()
            print doc_words
            print bow
            print "====================\n"
    return corpus

def create_feature_matrix(corpus, dictionary):
    feat_matrix = sp.sparse.dok_matrix((len(dictionary), len(corpus)), dtype=np.int)
    for doc_id, vector in enumerate(corpus):
        for (feature_idx, freq) in vector:
            feat_matrix[feature_idx, doc_id] = freq
    #print feat_matrix #print the matrix in the end and verify the counts in the corpus
    return feat_matrix


def main():
    dictionary = get_dict() #get the dictionary
    print "Unique tokens: %s" % len(dictionary) 
  
    corpus = create_features(dictionary, "corpus.txt") # iterate over the corpus and create the bag of words model now that you have the dictionary
    X = create_feature_matrix(corpus, dictionary)
    
if __name__ == "__main__":
    main()

