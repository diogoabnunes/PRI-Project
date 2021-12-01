import pandas as pd

races = pd.read_csv("../documentos_resultado/races_joined.csv")

print(races.isnull().sum())