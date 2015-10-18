import os
import subprocess

#base directory path 
BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)

#function implementation
def get_pmids():
   """Given a file list of pmids parse and return only the pmids

   Returns
   -------
   list
       The list of pmids in the file
   """
   
   #Initialize pmids as a list
   pmids = list()
   pmids_file = os.path.join(BASEDIR, 'data', 'PMIDS_IN_DATASET')
   #opening file for reading in binary mode
   with open(pmids_file, "rb") as f:
       lines = f.readlines()
       for line in lines:
           #strip and add the pmids from each line into the list
	   pmid = line.split()[2].strip()
	   #running an external command
           #Setting the shell argument to a true value causes subprocess to start an intermediate shell process, and tell it to run the command. 
           subprocess.call(["wget http://www.ncbi.nlm.nih.gov/pubmed/", pmid], shell=True)
           # print("%s\t%s" % (line, int(pmid)))
           pmids.append(pmid)
   # print(pmids)
   return pmids


#main method
def main():
#function call
    get_pmids();

if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it
