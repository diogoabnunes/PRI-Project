import pandas as pd
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

races = pd.read_csv('../F1_Data/races.csv')

paragraphs = []

urls = races['url']
raceId = 0

data = {'raceId' : [], 'paragraph' : []}

#719, 735

def cleanParagraph(s):
  if(s.name == 'p' and not re.match('^[*].*$', s.text)):
    for sup in s.findAll('sup'):
      sup.decompose()
    for a in s.findAll('a'):
      a.replaceWithChildren()
    for span in s.findAll('span'):
      span.decompose()
  else:
    return ''

  text = s.text.replace('\xa0','') 
  text = text.replace('\n','') 

  if(re.match('^  -',text)):
      text = text[3:]

  return text

for url in urls:
  raceId += 1
  html = urlopen(url)
  bs = BeautifulSoup(html,'html.parser')
  qualifying = bs.find('span', {'id': re.compile('.*[qQ]ualifying$')})

  # qualiying section
  if qualifying is not None:
    parent = qualifying.find_parent(re.compile('h[1-9]'))
    if parent is not None:
      s = parent.find_next_sibling('p')

      # paragraphs
      while(s is not None and not re.match('h[1-9]',s.name)):
        text = cleanParagraph(s)

        # not empty
        if text:
          data['raceId'].append(raceId)
          data['paragraph'].append(text)

        s = s.find_next_sibling()

df = pd.DataFrame(data=data)
df.to_csv('qualifying_text.csv',index=False)
