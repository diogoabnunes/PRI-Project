# Crawling 18 categories about F1

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

  if text.endswith(':'): text = ''
  elif text.startswith('(') and text.endswith(')'): text = ''
  elif text.startswith('*') or text.startswith('†') or text.startswith('‡'): text = ''
  elif not text.endswith('.'): text = ''

  return text

pages = pd.read_csv("../F1_Data/f1pages.csv")

pageIds = pages['pageId']
pageNames = pages['pageName']
urls = pages['url']

data = {'pageId': [], 'pageName': [], 'text': []}

for i in range(len(pages)):
    pageId = pageIds[i]
    pageName = pageNames[i]
    url = urls[i]
    print(f'pageName: {pageName}')

    html = urlopen(urls[i])
    bs = BeautifulSoup(html, 'html.parser')
    first_p = bs.p
    last = bs.find('span', {'id': 'See_also'})

    while (first_p is not None and first_p != last):
        if (first_p.name == 'p'):
            text = cleanParagraph(first_p)
            if text:
                data['pageId'].append(pageId)
                data['pageName'].append(pageName)
                data['text'].append(text) 
        first_p = first_p.find_next_sibling()

df = pd.DataFrame(data=data)
df.to_csv('../processed_data/pages_text.csv', index=False)