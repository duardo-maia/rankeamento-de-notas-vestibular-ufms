import pandas as pd
from decimal import Decimal

# Entrada do usuário
print('INFORME O COD do CURSO')
cod_curso = int(input())

print('INFORME A COTA')
cota = input()

print('CORTE')
corte =int(input())

print('1 = VL // 2 = VH // 3 = VN // 4 = VM // 5 = RED')

pesos = []
soma = 0
for i in range(5):
    print('INFORME O PESO: ', i + 1)
    peso = int(input())
    soma = peso + soma
    pesos.append(peso)

pesos.append(soma)
print('soma -> ', soma, pesos[0], pesos[1], pesos[2], pesos[3], pesos[4])

# Carregar os arquivos
arquivo_inscritos = "C:\\Users\\Eduar\\PycharmProjects\\PythonProject\\Vest\\.venv\\arquivos\\saida.xlsx"
df_inscritos = pd.read_excel(arquivo_inscritos)

base_notas = 'C:\\Users\\Eduar\\PycharmProjects\\PythonProject\\Vest\\.venv\\arquivos\\base_notas_2024.xlsx'
df_notas = pd.read_excel(base_notas)

# Filtrar inscritos com base no código do curso
filtroInscritos = []
matriz = []

for i in range(len(df_inscritos)):
    if df_inscritos.iloc[i, 2] == cod_curso and df_inscritos.iloc[i, 3] == cota:
        filtroInscritos.append([df_inscritos.iloc[i, 0], df_inscritos.iloc[i, 1]])

# Calcular a nota final e preencher a matriz
for i in range(len(filtroInscritos)):
    buscador = filtroInscritos[i][0]
    for j in range(len(df_notas)):
        if df_notas.iloc[j, 0] == buscador:
            vl = pesos[0] * Decimal(df_notas.iloc[j, 2].replace(",", "."))
            vh = pesos[1] * Decimal(df_notas.iloc[j, 3].replace(",", "."))
            vn = pesos[2] * Decimal(df_notas.iloc[j, 4].replace(",", "."))
            vm = pesos[3] * Decimal(df_notas.iloc[j, 5].replace(",", "."))
            red = pesos[4] * int(df_notas.iloc[j, 6])
            nota_final = (vl + vh + vn + vm + red) / soma
            matriz.append([buscador, filtroInscritos[i][1], float(nota_final)])

# Ordenar a matriz por nota_final em ordem decrescente
matriz.sort(key=lambda x: x[2], reverse=True)   

# Gerar o nome do arquivo de saída
output_file = f"C:\\Users\\Eduar\\PycharmProjects\\PythonProject\\Vest\\.venv\\arquivos\\resultado_{cod_curso}LP.txt"

# Salvar os resultados no arquivo
with open(output_file, "w") as f:
    i = 1
    f.write("--------- LISTA DE RANKEAMENTO EXTRAOFICIAL ------------\n")
    f.write("------------------- VESTIBULAR 2025 ---------------------\n")
    f.write(f"---------- COD-CURSO = {cod_curso} COTA = {cota} ----------\n")
    f.write("\n")
    f.write('RANK -- INSCRI -- NOME -- MEDIA\n')
    f.write('\n')
    for linha in matriz:
        if i == corte:
            f.write(f"{i} -- {linha[0]} -- {linha[1]} -- {linha[2]:.3f} <<<------- MEDIA CORTE\n")  # Três casas decimais na nota_final
        else:
            f.write(f"{i} -- {linha[0]} -- {linha[1]} -- {linha[2]:.3f}\n")
        i += 1

print(f"Resultados salvos em: {output_file}")

# Exibir a matriz ordenada
for linha in matriz:
    print(linha)
