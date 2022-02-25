import os
import glob
import pandas as pd
from nltk import tokenize

# final csvs path
source = "../final_csvs/"
destination = "../final_json/"

for file in glob.glob(os.path.join(source, '*.csv')):
  filename = file.split('/')[-1][:-4]
  filename_json = f'{filename}.json'

  df = pd.read_csv(file)

  for i, row in df.iterrows():
    if(filename != 'races'):
      if isinstance(row.text, str):
        df.at[i,'text'] = tokenize.sent_tokenize(row.text)
    else:
      # races.csv has different format
      # category,raceId,name,year,round,circuitId,date,time,url,qualifying_text,race_text
      if isinstance(row.race_text, str):
        df.at[i,'race_text'] = tokenize.sent_tokenize(row.race_text)
      if isinstance(row.qualifying_text, str):
        df.at[i,'qualifying_text'] = tokenize.sent_tokenize(row.qualifying_text)

  df.to_json(f'{destination}{filename_json}', orient='records')

