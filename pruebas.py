import pandas as pd
import numpy as np

df = pd.read_csv("players_20.csv")

#fijar index
df = df.set_index("short_name")
"""
Puedes sobreescribir el cambio como he hecho arriba o con inplace=True
df.set_index("short_name", inplace=True)
"""

print(df)