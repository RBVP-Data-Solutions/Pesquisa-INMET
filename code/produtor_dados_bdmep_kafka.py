from azure.storage.blob import BlobClient, BlobServiceClient
from kafka import KafkaProducer
import requests, zipfile, io
import json

# VARIÁVEIS DE APOIO
cadeia_conexao = str(open('cadeia_conexao.txt', 'r'))
nome_container = 'bdmep'

# CONEXÃO COM DATA LAKE
blob_service_client = BlobServiceClient.from_connection_string(cadeia_conexao)
container_client = blob_service_client.get_container_client(nome_container)

# CONEXÃO COM KAFKA
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# EXTRAÇÃO DOS DADOS DO BDMEP(BANCO DE DADOS METEREOLOGICOS)
response = requests.get('https://bdmep.inmet.gov.br/$2a$10$mwzyjeScvWM7EvtZ3Z1ZDezZWIZTzRcbdMNULILAmfFQeNQD07LXe.zip')

# ENVIANDO OS DADOS PARA O KAFKA CONSUMER
if response.status_code == 200:
    data = response.json()
    producer.send('dados-bdmep', data)
    producer.flush()
    print("Dados enviados para o Kafka.")
else:
    print("Erro ao acessar a API:", response.status_code)

producer.close()
