# Crawling circuits

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
  text = text.strip()
  return text

circuits = pd.read_csv("../F1_Data/circuits.csv")

circuitIds = circuits['circuitId']
urls = circuits['url']

data = {'circuitId': [], 'text': []}

for i in range(len(circuits)):
    circuitId = circuitIds[i]
    print(f'circuitID: {circuitId}')
    url = urls[i]

    html = urlopen(urls[i])
    bs = BeautifulSoup(html, 'html.parser')
    first_p = bs.p
    # fix circuit 26 having a different format from the rest
    if(first_p and circuitId == 26):
      first_p = first_p.find_next('p')

    last = bs.find('span', {'id': 'See_also'})

    while (first_p is not None and first_p != last):
        if (first_p.name == 'p'):
            text = cleanParagraph(first_p)
            if text and text != '(key)':
                data['circuitId'].append(circuitId)
                data['text'].append(text) 
        first_p = first_p.find_next_sibling()


df = pd.DataFrame(data=data)
df.to_csv('../processed_data/circuits_text.csv', index=False)
