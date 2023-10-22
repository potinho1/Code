import pymysql
import dotenv
import os

# Carrega variaveis de ambiente 
dotenv.load_dotenv()

# Conecta no banco de dadaos e usa as credenciais de=o arquivo env
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

# Criando a tabela 'customers' se ela não existir
# conexao com o banco
with connection:
    # Criando a função cursor
    with connection.cursor() as cursor:
      # Executa a criação da tabela, se ela não existir
      cursor.execute(
        'CREATE TABLE ID NOT EXISTS customers ('
        'id INT NOT NULL AUTO_INCREMENT, '
        'nome VARCHAR(50) NOT NULL, '
        'idade INT NOT NULL, '
        'PRIMARY KEY (id)'
        ') '
      )
      # Confirma as alterações feitas no banco
      connection.commit()
      print(cursor)
