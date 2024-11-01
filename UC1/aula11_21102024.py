import pandas as pd

df_evasao = pd.read_csv('evasão_escolar.csv')
print(df_evasao.head())
print(df_evasao.tail())

import pandas as pd

df_spotify = pd.read_csv('spotify_2024.csv', encoding='UTF-8', on_bad_lines='skip', error_bad_lines=False)
print(df_spotify.head())
print(df_spotify.tail())


import pandas as pd

df_exterior=pd.read_csv('exterior.csv')
print(df_exterior.head(5))
