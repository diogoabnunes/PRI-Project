import pandas as pd

## ler csv
constructors = pd.read_csv("../F1_Data/constructors.csv")
constructors_text = pd.read_csv("../processed_data/constructors_text.csv")

constructors_df = constructors_text.groupby(['constructorId'], as_index = False).agg({'text': '\n'.join})

## merge
constructors_joined = pd.merge(constructors, constructors_df, on="constructorId", how="left")
#constructors_joined = constructors_joined.rename(columns={'text': 'constructors_text'})


## escrever num csv
print(constructors_joined)
constructors_joined.to_csv("../documentos_resultado/constructors_joined.csv", index=False)