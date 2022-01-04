# Crawling seasons

import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def cleanParagraph(s):
  if(s.name == 'p'):
    for sup in s.findAll('sup'):
      sup.decompose()
    for a in s.findAll('a'):
      a.replaceWithChildren()
  else:
    return ''

  text = s.text.replace('\xa0','') 
  text = text.replace('\n','') 
  text = text.replace('(key)','')
  text = text.replace('* Season still in progress.','')
  text = text.replace('(*) Season still in progress.','')  
  text = text.replace('Notes:','')
  text = text.strip()

  if text.endswith(':'): text = ''
  elif text.startswith('(') and text.endswith(')'): text = ''
  elif text.startswith('*') or text.startswith('†') or text.startswith('‡'): text = ''
  elif not text.endswith('.'): text = ''

  return text

seasons = pd.read_csv("../F1_Data/seasons.csv")

seasonIds = seasons['year']
urls = seasons['url']

data = {'year': [], 'text': []}

for i in range(len(seasons)):
    seasonId = seasonIds[i]
    print(f'seasonID: {seasonId}')
    url = urls[i]

    html = urlopen(urls[i])
    bs = BeautifulSoup(html, 'html.parser')
    first_p = bs.p
    last = bs.find('span', {'id': 'See_also'})

    while (first_p is not None and first_p != last):
        if (first_p.name == 'p'):
            text = cleanParagraph(first_p)
            if text and text != '(key)':
                data['year'].append(seasonId)
                data['text'].append(text) 
        first_p = first_p.find_next_sibling()

df = pd.DataFrame(data=data)
df.to_csv('../processed_data/seasons_text.csv', index=False)