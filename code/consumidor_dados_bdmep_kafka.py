from kafka import KafkaConsumer
from azure.storage.filedatalake import DataLakeServiceClient

# VARIÁVEIS DE APOIO
cadeia_conexao = str(open('cadeia_conexao.txt', 'r'))
nome_container = 'bdmep'

# CONEXÃO COM O AZURE DATA LAKE GEN 2
service_client = DataLakeServiceClient.from_connection_string(cadeia_conexao)
file_system_client = service_client.get_file_system_client(nome_container)

# RECEBENDO OS DADOS DO KAFKA PRODUCER
consumer = KafkaConsumer('dados-bdmep', bootstrap_servers='localhost:9092')

# EXTRAINDO OS DADOS PARA A CAMADA BRONZE DO DATA LAKE
for message in consumer:
    data = message.value.decode('utf-8')
    # Armazenando no Data Lake
    file_client = file_system_client.get_file_client('bronze/')
    file_client.upload_data(data, overwrite=True)
