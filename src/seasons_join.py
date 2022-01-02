import pandas as pd

## ler csv
seasons = pd.read_csv("../F1_Data/seasons.csv")
seasons_text = pd.read_csv("../processed_data/seasons_text.csv")

seasons_df = seasons_text.groupby(['year'], as_index = False).agg({'text': '\n'.join})

## merge
seasons_joined = pd.merge(seasons, seasons_df, on="year", how="left")


## escrever num csv
print(seasons_joined)
seasons_joined.to_csv("../documentos_resultado/seasons_joined.csv", index=False)