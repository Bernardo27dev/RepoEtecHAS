import pyodbc # pip install pyodbc
import pandas as pd # pip install pandas
# python.exe -m pip install --upgrade pip
from os import system

try:
    # identificações
    server = 'localhost'
    database = 'petshop'
    username = 'sa'
    password = '*123456HAS*'
    # Conexão
    # conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=' + server + ';DATABASE=' + database + ';Uid=' + username + ';PWD=' + password)
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
    3 - Buscar Pets
    4 - Editar Pet
    5 - Excluir Pet
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
                idade = int(input("idade............."))
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
        case 2:
            lista_dados = []
            inst_consulta.execute("select * from petshop")
            data = inst_consulta.fetchall()

            for dt in data:
                lista_dados.append(dt)
            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,
                                                 columns=['id', 'Tipo', 'Nome', 'idade'], index='id')
            
            if dados_df.empty:
                print("Sem dados")
            else:
                print(dados_df)
        case 3:
            lista_dados = []
            print('Buscar cadastro')
            idPet = int(input("id: "))
            inst_consulta.execute(f"select * from petshop where id = {idPet}")
            data = inst_consulta.fetchall()  
            
            if data == "" or data == None:
                print("Sem dados")
            else:
                for dt in data:
                    lista_dados.append(dt)
                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['id', 'Tipo', 'Nome', 'idade'], index='id')
                print(dados_df)
        case 4:
            lista_dados = []
            print('Buscar cadastro')
            idPet = int(input("id: "))
            inst_consulta.execute(f"select * from petshop where id = {idPet}")
            data = inst_consulta.fetchall()  

            
            
            if data == "" or data == None:
                print("Sem dados")
            else:
                for dt in data:
                    lista_dados.append(dt)
                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['id', 'Tipo', 'Nome', 'idade'], index='id')
                try:
                    print(f"Dados Anteriores:\n{dados_df}")
                    print("EDITANDO PET")
                    tipo = input("Tipo.............")
                    nome = input("Nome.............")
                    idade = int(input("idade............."))
                    print(tipo)
                    edit = f"""
                    UPDATE petshop
                    SET tipo_pet = '{tipo}', nome_pet = '{nome}', idade = {idade} WHERE id = {idPet}
                    """
                    inst_cadastro.execute(edit)
                    conn.commit()
                except ValueError:
                    print("idade deve ser numerico")
                else:
                    print("Editado com sucesso!")
        case 5:
            print('Deletar cadastro')
            idPet = int(input("id: "))
            inst_consulta.execute(f"select nome_pet from petshop where id = {idPet}")
            data = inst_consulta.fetchone()    

            if data == "" or data == None:
                print("Sem dados")
            else:
                while True:
                    opt = str(input(f"Deseja deletar o cadastro do {data[0]} Y/N"))
                    match opt.lower():
                        case 'y':
                            inst_consulta.execute(f"delete from petshop where id = {idPet}")
                            print("Deletado.")
                            break
                        case 'n':
                            print("Canncelado.")
                            break
                        case _:
                            print("Opção Inválida.")
        case _:
            print("Escolha uma opção válida.")
    input("Pressione qualquer tecla para continuar")