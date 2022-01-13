import pandas as pd

## ler csv
pages_text = pd.read_csv("../processed_data/pages_text.csv")

pages_df = pages_text.groupby(['pageId'], as_index = False).agg({'text': '\n'.join})


## escrever num csv
print(pages_df)
pages_df.to_csv("../documentos_resultado/pages_text.csv", index=False)