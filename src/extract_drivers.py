# Crawling drivers

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
  text = text.replace('Season still in progress.', '')
  text = text.replace('* Season still in progress.','')
  text = text.replace('† Not eligible for points', '')
  text = text.replace('‡ Not eligible for points.', '')
  text = text.replace('(*) Season still in progress.','')  
  text = text.replace('(Races in bold indicate pole position; races in italics indicate fastest lap)', '')
  text = text.strip()

  if text.endswith(':'):
    text = ''
  elif text.startswith('(') and text.endswith(')'):
    text = ''
  elif text.startswith('*') or text.startswith('†') or text.startswith('‡'):
    text = ''
  elif not text.endswith('.'):
    text = ''


  return text

drivers = pd.read_csv("../F1_Data/drivers.csv")

driverIds = drivers['driverId']
urls = drivers['url']

data = {'driverId': [], 'text': []}

for i in range(len(drivers)):
    driverId = driverIds[i]
    print(f'DriverID: {driverId}')
    url = urls[i]
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    first_p = bs.p
    pclass = None

    # fix empty paragraph recently added to some driver's wikipedia pages
    if first_p and first_p.has_attr('class'):
      pclass =  first_p['class'][0]
      if(pclass == 'mw-empty-elt'):
        first_p = first_p.find_next('p')

    last = bs.find('span', {'id': 'See_also'})

    while (first_p is not None and first_p != last):
        if (first_p.name == 'p'):
            text = cleanParagraph(first_p)
            if text:
                data['driverId'].append(driverId)
                data['text'].append(text) 
        first_p = first_p.find_next_sibling()

df = pd.DataFrame(data=data)
df.to_csv('../processed_data/drivers_text.csv', index=False)
