from bs4 import BeautifulSoup
import os
import subprocess

#base directory path
# BASEDIR="/home/nishita/resqu/data/documentCorpus/"
BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
pmids_file = os.path.join(BASEDIR, 'data', 'documentCorpus/')
print(pmids_file)
#BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)


for file in os.listdir(pmids_file):
     print(file)
     filepath = os.path.join(pmids_file, file)
     print(filepath)
     soup = BeautifulSoup(open(filepath),"html.parser")

     # for strong_tag in soup.find_all('h3'):
     #      if strong_tag.text == 'Abstract' :
     #          print strong_tag.next_sibling.text
     #          break

     result = soup.findAll("a", {"title": "National Library of Medicine"})

     for results in result :
         print(result)



     # for strong_tag in soup.findAll('a', {'alterm' : 'Radiology'}):
     #     # if strong_tag.text == 'Abstract' :
     #     print strong_tag.next_sibling.text
     #     break
