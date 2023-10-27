import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

# Carrega variaveis de ambiente 
dotenv.load_dotenv()

# Conecta no banco de dadaos e usa as credenciais de=o arquivo env
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

# Criando a tabela 'customers' se ela não existir
# conexao com o banco
with connection:
    # Criando a função cursor
    with connection.cursor() as cursor:
      # Executa a criação da tabela, se ela não existir
      cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
        'id INT NOT NULL AUTO_INCREMENT, '
        'nome VARCHAR(50) NOT NULL, '
        'idade INT NOT NULL, '
        'PRIMARY KEY (id) '
        ') '
      )
      # Confirma as alterações feitas no banco
      cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') # Limpa a tabela
    connection.commit()

    # Criando a função cursor
    with connection.cursor() as cursor:
      # Inserindo dados na tabela
      result = cursor.execute(
        f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) VALUES ("Potinho", 22)'
      )
      print(result)
      # Inserindo dados na tabela
      result = cursor.execute(
        f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) VALUES ("João", 23)'
      )
      print(result)
      # Inserindo dados na tabela
      result = cursor.execute(
        f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) VALUES ("Vitor", 24)'
      )
      print(result)
      # Confirma as alterações feitas no banco
    connection.commit()
