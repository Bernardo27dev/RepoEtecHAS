import pyodbc # pip install pyodbc
import pandas as pd # pip install pandas
# python.exe -m pip install --upgrade pip
from os import system

try:
    # identificações
    server = 'localhost'
    database = 'teste'
    username = 'sa'
    password = '*123456HAS*'
    # Conexão
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=' + server + ';DATABSE=' + database + ';UID=' + username + ';PWD=' + password)
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    print("Conexão estabelecida!")
    conexao = True

while conexao:
    system("cls")
    # Menu
    print("""
    MENU
    0 - Sair
    1 - Cadastrar Pet
    2 - Listar Pets
    """)
    escolha = int(input("Escolha: "))
    system("cls")
    match escolha:
        case 0:
            conexao = False
        case 1:
            try:
                print("CADASTRANDO PET")
                tipo = input("Tipo.............")
                nome = input("Nome.............")
                idade = int(input("Idade............."))
                cadastro = f"""
                INSERT INTO petshop (tipo_pet, nome_pet, idade)
                VALUES ('{tipo}','{nome}',{idade})
                """
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                print("idade deve ser numerico")
            else:
                print("Cadastro com sucesso!")
#         case 2:
#             lista_dados = []
#             inst_consulta.execute("select * from petshop")
#             data = inst_consulta.fetchall()

#             for dt in data:
#                 lista_dados.append(dt)
#             lista_dados = sorted(lista_dados)

#             dados_df = pd.DataFrame.from_records(lista_dados,
#                                                  columns=['Id', 'Tipo', 'Nome', 'Idade'], index='Id')
#             # dataframe copia os dados numa planilha virtual (como se fosse um excel)
#             if dados_df.empty:
#                 print("Sem dados")
#             else:
#                 print(dados_df)
        
    input("\nPressione qualquer tecla para continuar")