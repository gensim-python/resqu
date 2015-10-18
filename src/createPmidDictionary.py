import os
import subprocess

BASEDIR = os.path.join(os.path.dirname(__file__))#, os.path.pardir)
print("basedir : ",BASEDIR)

#def main():
#    get_pmids();

def get_pmids():
   """Given a file list of pmids parse and return
   only the pmids

   Returns
   -------
   list
       The list of pmids in the file
   """
   print("basedir : ",BASEDIR)
   pmids = list()
   print("hello",pmids)
   pmids_file = os.path.join(BASEDIR, 'data', 'PMIDS_IN_DATASET')
   print(pmids_file)
   with open(pmids_file, "rb") as f:
       lines = f.readlines()
       for line in lines:
           pmid = line.split()[2].strip()
           print(pmid)
           subprocess.call(["wget http://www.ncbi.nlm.nih.gov/pubmed/", pmid], shell=True)
           # print("%s\t%s" % (line, int(pmid)))
           pmids.append(pmid)
   # print(pmids)
   return pmids



def main():
    get_pmids();

if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it
