import sqlite3
from pathlib import Path

# Sempre vai buscar o diretorio que o "main.py" estiver localizado
ROOT_DIR = Path(__file__).parent
# Crio o nome do arquivo de banco de dados
DB_NAME = 'db.sqlite3'
# Junto o diretorio e o nome onde eu vou cirar o BD
DB_FILE = ROOT_DIR / DB_NAME
# Criando o nome da tabela
TABLE_NAME = 'customers'

# Abro a conexao com o banco
connection = sqlite3.connect(DB_FILE)
# executa comandos SQL
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


if __name__ == '__main__':
    print(sql)

# DELETE 
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME} '
#     'WHERE id = 1'
# )

#UPDATE
cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="QUALQUER" '
    'WHERE id = 2'
)

connection.commit()

cursor.close()
connection.close()


'''
CRUD = CREATE-READ-UPDATE-DELETE

SQL = INSERT-SELECT-UPDATE-DELETE

Nunca faça um UPDATE sem o WHERE

Nunca fazer um DELETE sem o WHERE 
'''