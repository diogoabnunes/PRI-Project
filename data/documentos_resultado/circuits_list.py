import pandas as pd

circuits_joined = pd.read_csv('../final_csvs/circuits.csv')

circuits_joined.text
circuits_joined.text=circuits_joined.text.str.split('.').tolist()


circuits_joined.to_json('circuits_list_table.json', orient='table', index=False)
circuits_joined.to_json('circuits_list_split.json', orient='split', index=False)
