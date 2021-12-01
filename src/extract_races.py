import pandas as pd
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

races = pd.read_csv('../F1_Data/races.csv')

paragraphs = []

urls = races['url']
racesId = races['raceId']

data = {'raceId' : [], 'paragraph' : []}


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
  return text

for url,raceId in zip(urls,racesId):
  print(raceId)
  html = urlopen(url)
  bs = BeautifulSoup(html,'html.parser')
  first_p = bs.p
  span = bs.find('span', {'id': re.compile('Race.*')})
  qualifying = bs.find('span', {'id': 'Qualifying'})

  # first paragraphs
  while(first_p is not None and not re.match('h[1-9]',first_p.name)):
    if(first_p.name == 'p' and first_p.find('span') is None):
      text = cleanParagraph(first_p)
      if text:
        data['raceId'].append(raceId)
        data['paragraph'].append(text)

    first_p = first_p.find_next_sibling()

  # race sections
  if span is not None:
    parent = span.find_parent(re.compile('h[1-9]'))
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
df.to_csv('../processed_data/race_text.csv',index=False)
