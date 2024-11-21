import pyodbc
import pandas as pd
import os
from time import sleep

try:
    server = 'pets_database.mssql.somee.com'
    database = 'pets'
    username = 'Vini_dev_SQLLogin_1'
    password = 'kov33gmdsc'
    conn = pyodbc.connect('DRIVER={SQL Server};'
        'SERVER=pets_database.mssql.somee.com;'
        'DATABASE=pets_database;'
        'UID=Vini_dev_SQLLogin_1;'
        'PWD=kov33gmdsc;'
        'TrustServerCertificate=True;'
        'Persist Security Info=False;'
        'Packet Size=4096;')
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as error:
    print('Error: Could not connect to the database.', error)
    exit()
    conexao = False
else:
    print("connected to database")
    conexao = True

print("Bem vindo ao petshop")
# print("""
# ⠀⠀⠀⠀⠀⢀⡴⠋⠉⠛⠒⣄⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢸⠏⠀⠀⣶⡄⠀⠀⣛⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⡤⠋⠠⠉⠡⢤⢀⠀
# ⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢉⣝⠲⠤⣄⣀⣀⠌
# ⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀
# ⢀⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀
# ⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀
# """)

while True:
    print("\nO que deseja fazer?\n0 - Sair\n1 - Cadastrar um novo pet\n2 - Listar Pets\n3 - Buscar Pet\n4 - Editar Pet\n5 - Excluir Pet\n")
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Opção inválida. Tente novamente.")
        continue
    match opcao:
        case 1:
            try:
                try:
                    print("Você escolheu a opção 1 - Cadastrar um novo pet\n")
                    nome = str(input("Digite o nome do pet:"))
                    tipo = input("Digite o tipo do pet:")
                    idade = int(input("Digite a idade do pet:"))
                except ValueError:
                    print("Nome inválido. Tente novamente.")
                    continue
                try:
                    inst_cadastro.execute("INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES (?,?,?)", tipo, nome, idade)
                    conn.commit()
                    print("Pet cadastrado com sucesso.")
                except Exception as error:
                    print("Ocorreu um erro ao cadastrar", error)
            except Exception as error:
                print('Error: ocorreu um erro na aplicação.', error)
                exit()
        case 2:
            print("")
        case 3:
            try:
                try:
                    print("Você escolheu a opção 3 - Buscar por um Pet\n")
                    nome_pet = str(input("Digite o nome do pet que deseja consultar:"))
                except ValueError as error:
                    print("Nome inválido. Tente novamente.", error)
                    continue
                try:
                    pet_content = []
                    inst_consulta.execute("SELECT * FROM petshop WHERE nome_pet =?", nome_pet)
                    data = inst_consulta.fetchall()

                    for dt in data:
                        pet_content.append(dt)
                    pet_content = sorted(pet_content)

                    dados_df = pd.DataFrame.from_records(pet_content, columns=["Id", "Tipo", "Nome", "Idade"])

                    if dados_df.empty:
                        print("Pet não encontrado.")
                    else:
                        print("\nResultado da consulta:")
                        print(dados_df)
                except Exception as error:
                    print("Erro ao consultar o pet", error)
            except Exception as error:
                print('Error: ocorreu um erro na busca por pets.', error)
                exit()
        case 0:
            print("Programa encerrado.")
            conn.close()