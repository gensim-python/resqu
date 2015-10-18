import os
import subprocess

BASEDIR = os.path.join(os.path.dirname(__file__), "..")

def get_pmids():
   """Given a file list of pmids parse and return
   only the pmids

   Returns
   -------
   list
       The list of pmids in the file
   """
   pmids = list()
   pmids_file = os.path.join(BASEDIR, 'data', 'PMIDS_IN_DATASET')
   with open(pmids_file, "rb") as f:
       lines = f.readlines()
       for line in lines:
           pmid = line.split()[2].strip()
           subprocess.call(["wget http://www.ncbi.nlm.nih.gov/pubmed/", pmid], shell=True)
           # print("%s\t%s" % (line, int(pmid)))
           pmids.append(pmid)
   # print(pmids)
   return pmids


def main():
   get_pmids()

