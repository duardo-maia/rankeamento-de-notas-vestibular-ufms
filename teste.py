import pandas as pd


# Caminho do arquivo Excel de entrada
arquivo = "C:/Users/Eduar/PycharmProjects/PythonProject/Vest/.venv/arquivos/nome_candidatos_codcurso_2024.xlsx"

# Carrega o Excel
df = pd.read_excel(arquivo)

# Lista para armazenar os dados processados
saida_dados = []

# Processamento
index_num_isncri = 0
index_cota = 0
for i in range(len(df)):
    linha = df.iloc[i, 0]
    if type(linha) == str:
        teste = linha[0:2]
        teste_ponto = linha[2]
        if (teste == '10' or teste == '11') and (teste_ponto != '.'):
            partes = linha.split()
            for parte in range(len(partes)):
                try:
                    num_inscri = int(partes[parte])
                    partes[parte] = num_inscri
                    index_num_isncri = parte
                except ValueError:
                    pass

                aux = partes[parte]
                if type(aux) == str:
                    try:
                        if aux == 'AC' or aux[2] == "_":
                            index_cota = parte
                    except IndexError:
                        pass

            # Adiciona os dados processados à lista
            saida_dados.append([partes[0], partes[1], partes[index_num_isncri], partes[index_cota]])

# Caminho do arquivo de saída
arquivo_saida_excel = "C:/Users/Eduar/PycharmProjects/PythonProject/Vest/.venv/arquivos/saida.xlsx"

# Cria um DataFrame com os dados processados
df_saida = pd.DataFrame(saida_dados, columns=['NRO_INSCRI', 'P_NOME', 'COD_CURSO', 'COTA'])

# Salva o DataFrame em um arquivo Excel
df_saida.to_excel(arquivo_saida_excel, index=False)

print(f"Dados processados salvos em: {arquivo_saida_excel}")
