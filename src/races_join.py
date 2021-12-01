import pandas as pd

## ler csv
races = pd.read_csv("../F1_Data/races.csv")
race_text = pd.read_csv("../processed_data/race_text.csv")
qualifying_text = pd.read_csv("../processed_data/qualifying_text.csv")

qualifying_df = qualifying_text.groupby(['raceId'], as_index = False).agg({'paragraph': '\n'.join})
race_df = race_text.groupby(['raceId'], as_index = False).agg({'paragraph': '\n'.join})

## merge
races_joined = pd.merge(races, qualifying_df, on="raceId", how="left")
races_joined = races_joined.rename(columns={'paragraph': 'qualifying_text'})
races_joined = pd.merge(races_joined, race_df, on="raceId", how="left")
races_joined = races_joined.rename(columns={'paragraph': 'race_text'})

## escrever num csv
print(races_joined)
races_joined.to_csv("../documentos_resultado/races_joined.csv", index=False)