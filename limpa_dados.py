import pandas as pd

# Caminho do arquivo Excel
arquivo = "C:/Users/Eduar/PycharmProjects/PythonProject/Vest/.venv/arquivos/nome_candidatos_codcurso_2024.xlsx"

# Carrega o Excel
df = pd.read_excel(arquivo)

# Caminho do arquivo de saída
arquivo_saida = "C:/Users/Eduar/PycharmProjects/PythonProject/Vest/.venv/arquivos/saida.txt"

index_num_isncri = 0
index_cota = 0;
with open(arquivo_saida, 'w') as file:
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

                print(partes[0], partes[index_num_isncri])
                file.write(f"{partes[0], partes[1], partes[index_num_isncri], partes[index_cota]}\n")   