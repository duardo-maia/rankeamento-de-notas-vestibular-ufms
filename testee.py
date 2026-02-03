import pandas as pd
from decimal import Decimal

base_notas = 'C:\\Users\\Eduar\\PycharmProjects\\PythonProject\\Vest\\.venv\\arquivos\\base_notas_2024.xlsx'
df_notas = pd.read_excel(base_notas)

teste = Decimal(df_notas.iloc[0,2].replace(",", "."))
mostra = df_notas.iloc[0,2]

print(mostra)

