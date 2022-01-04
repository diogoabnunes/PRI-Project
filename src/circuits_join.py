import pandas as pd

circuits = pd.read_csv("../F1_Data/circuits.csv")
circuits_text = pd.read_csv('../processed_data/circuits_text.csv')

circuits_df = circuits_text.groupby(['circuitId'], as_index=False).agg({'text': '\n'.join})

circuits_joined = pd.merge(circuits, circuits_df, on="circuitId", how="left")

circuits_joined.to_csv('../documentos_resultado/circuits_joined.csv', index=False)
