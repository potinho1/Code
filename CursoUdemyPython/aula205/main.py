import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where

'''
Se quiser apagar os id da tabela

curso.execute(
    f'DELETE FROM sqlite_sequence WHWRE name="{TABLE_NAME}"'
)
connection.commit()
'''
 
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

# Reristrando os valores na tabela 
# CUIDADO SE ESTIVER RECEBENDO OS VALORES DO USUARIOS NÃO FAÇA DESSE JEITO, PODE FACILITAR O SQL INJECTION
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Potinho", 9.9)'
)

connection.commit()

cursor.close()
connection.close()