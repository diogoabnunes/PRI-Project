import pandas as pd

circuits = pd.read_csv('../processed_data/circuits_text.csv')

circuit_df = circuits.groupby(['circuitId'], as_index=False).agg({'text': '\n'.join})

circuit_df.to_csv('../documentos_resultado/circuits_joined.csv', index=False)
