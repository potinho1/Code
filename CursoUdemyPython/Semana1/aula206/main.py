import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

teste = "Potinuopooooo"

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
      sql = (f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES'
            '(%(nome)s, %(idade)s)'
          )
      data = { 
         "nome": teste,
         "idade": 22,
      }
      # Inserindo dados na tabela
      result = cursor.execute(sql, data)
      # print(sql,data)
      # print(result)
      # Confirma as alterações feitas no banco
    connection.commit()

    # Criando a função cursor
    with connection.cursor() as cursor:
      sql = (f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES'
            '(%(nome)s, %(idade)s)'
          )
      data1 = ({ 
         "nome": "Poti",
         "idade": 22,
      },
      {
        "nome": "João",
        "idade": 90 
      })
      result1 = cursor.executemany(sql, data1)
      connection.commit()
