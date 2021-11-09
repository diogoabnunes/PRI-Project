import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

races = pd.read_csv('../F1_Data/races.csv')

paragraphs = []

urls = races['url']
raceId = 0

data = {'raceId' : [], 'paragraph' : []}

for url in urls:
  raceId += 1
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

          text = s.text.replace('\n','') 
          data['raceId'].append(raceId)
          data['paragraph'].append(text)

        s = s.find_next_sibling()


df = pd.DataFrame(data=data)
df.to_csv('race_text.csv',index=False)
