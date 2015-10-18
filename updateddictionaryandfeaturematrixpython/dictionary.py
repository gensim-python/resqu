from gensim.corpora import Dictionary

class DictionaryBuilder(object):

    def __init__(self, dictionary=None, corpus_file="citations-all.txt"):
        if dictionary == None:
            self.dictionary = self.create_dict(corpus_file)        
        else:
            self.dictionary = Dictionary.load(dictionary)

    def create_dict(self, corpus_file):
        dictionary = Dictionary();
        with open(corpus_file,"rb") as infile:
            lines = infile.readlines() #reads single line from file
		
            for line in lines:
                doc = line  #.split() #doc as bag of words (bow) of tokens in this line            
                dictionary.add_documents([doc])
        infile.close()
        
        return dictionary

