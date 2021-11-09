import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

races = pd.read_csv('../F1_Data/races.csv')

paragraphs = []

urls = races['url']

for url in urls:
  html = urlopen(url)
  bs = BeautifulSoup(html,'html.parser')
  span = bs.find("span",{'id': 'Race'})

  if span is not None:
    parent = span.find_parent('h3')
    if parent is not None:
      s = parent.find_next_sibling('p')

      while(s is not None and (s.name == 'p' or s.name == 'div')):
        if(s.name == 'p'):
          for sup in s.findAll('sup'):
            sup.decompose()
          for a in s.findAll('a'):
            a.replaceWithChildren()

          # output to database here
          print(s.text)

        s = s.find_next_sibling()
