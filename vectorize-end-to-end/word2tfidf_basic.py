import numpy as np
import os, json, ast
from gensim import corpora
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.matutils import corpus2dense

class TfidfLoader(object):
    def __init__(self, filepath=None, dictionary=None, tfidfmodel=None):
        if not os.path.exists(filepath):
            print("File path does not exist %s", filepath)
        else: 
            if not dictionary:
                dictionary = self.load_dictionary(filepath)  
            if not tfidfmodel:
                tfidfmodel = TfidfModel(dictionary=dictionary)

        self._dictionary = dictionary
        self._tfidfmodel = tfidfmodel
        
    def load_dictionary(self, filepath):
        dictionary = Dictionary() 
        with open(filepath, "rb") as f: 
            for line in f.readlines():
                # example = SampleTrainingExample(line)
                # context = example.context
                dictionary.add_documents([[word.lower() for word in line.split()]])
        return dictionary

    @property
    def dictionary(self):
        return self._dictionary

    @property
    def tfidfmodel(self):
        return self._tfidfmodel
    
class SampleTrainingExample(object):
    def __init__(self, context):
        doc = ast.literal_eval(str(context))
        self._url = doc['url']
        self._label = doc['label']
        self._page_context = doc['page_context']
        self._entity_context = doc['entity_context']

        self._context = self.get_context()

    @property
    def url(self):
        return self._url

    @property
    def context(self):
        return self._context
    
    @property
    def page_context(self):
        return self._page_context
    
    @property
    def entity_context(self):
        return self._entity_context
    
    @property
    def entity_uri(self):
        return self._entity_uri
    
    @property
    def label(self):
        return self._label
    
    def get_context(self):
        return self._page_context + self._entity_context

def get_training_examples(filepath):
    """Generate the weighted training examples matrix using tfidf
    and the labels for each example

    Parameters
    ----------
    filepath : str
        path to the training data

    Returns
    -------
    tuple of numpy arrays: X, y
        Weighted training examples
        Labels for each example 
    """
    tfidfloader = TfidfLoader(filepath)
    dictionary = tfidfloader.dictionary
    dictionary = corpora.Dictionary.load(os.path.join("..","data","jan-31-abs-without-GS.dict"))
    print "dict len :",len(dictionary)

    tfidfmodel = tfidfloader.tfidfmodel

    corpus = list() 
    labels = list()
    with open(filepath, "rb") as f:
        for line in f.readlines():
            # example = SampleTrainingExample(line)
            # context = example.context
            # label = example.label
            words = line.lower().split()
            doc = dictionary.doc2bow(words)
            tfidf_doc = tfidfmodel[doc]
            corpus.append(tfidf_doc)
            # labels.append(label)

    X = corpus2dense(corpus, num_terms=len(dictionary)).T
    y = np.array(labels)

    return X, y

if __name__ == "__main__":
    filepath = os.path.join("..", "data", "01-Acute_Appendicitis_ABS.txt")
    print("Creating tfidf vectors...")
    X, y = get_training_examples(filepath)
    print(X)
    # print(y)
    print("Number of Examples: %i\nNumber of dimensions: %i" % (X.shape[0], X.shape[1]))