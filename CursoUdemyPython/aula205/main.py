import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where

''''''
#Se quiser apagar os id da tabela
# Deleta a tabela e o que tem nela
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Apaga a sequencia de ID
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

 
# Cria a tabela 
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()
'''
# Reristrando os valores na tabela 
# CUIDADO SE ESTIVER RECEBENDO OS VALORES DO USUARIOS NÃO FAÇA DESSE JEITO, PODE FACILITAR O SQL INJECTION
# Aqui eu escrevo os dentro do sql os valores
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Potinho", 101)'
)
'''
# Já nesse codigo ele é mais seguro pq eu separo o que é codigo e valor
sql = (
    f'INSERT INTO {TABLE_NAME} ' 
    '(name, weight) '
    'VALUES '
    '(:nome, :idade)'   
)
# Esse comando permite que você mande mais de um conjunto de dados
#cursor.executemany(sql, [['Potinho', 10], ['João', 11]])

# Trabalhando com dicionarios 
cursor.execute(sql, {'nome': 'PotinhoJoao', 'idade': 190})

cursor.executemany(sql, [
    {'nome': 'PotinhoJoao', 'idade': 190},
    {'nome': 'joao', 'idade': 11},
    {'nome': 'Vitor', 'idade': 9},


])



connection.commit()

cursor.close()
connection.close()