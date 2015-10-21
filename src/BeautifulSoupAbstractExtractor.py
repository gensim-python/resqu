from bs4 import BeautifulSoup
import os
import subprocess

#base directory path
BASEDIR="/home/nishita/resqu/data/documentCorpus/"
#BASEDIR = os.path.join(os.path.dirname(__file__), os.path.pardir)


for file in os.listdir("data"):
     print(file)
     filepath = os.path.join(BASEDIR, file)
     print(filepath)
     soup = BeautifulSoup(open(filepath),"html.parser")

     for strong_tag in soup.find_all('h3'):
          if strong_tag.text == 'Abstract' :
              print strong_tag.next_sibling.text
              break
