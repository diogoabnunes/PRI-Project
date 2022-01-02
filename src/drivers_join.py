import pandas as pd

## ler csv
drivers = pd.read_csv("../F1_Data/drivers.csv")
drivers_text = pd.read_csv("../processed_data/drivers_text.csv")

drivers_df = drivers_text.groupby(['driverId'], as_index = False).agg({'text': '\n'.join})

## merge
drivers_joined = pd.merge(drivers, drivers_df, on="driverId", how="left")
#drivers_joined = drivers_joined.rename(columns={'text': 'drivers_text'})


## escrever num csv
print(drivers_joined)
drivers_joined.to_csv("../documentos_resultado/drivers_joined.csv", index=False)