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

producer = KafkaProducer(bootstrap_servers='localhost:9092')

response = requests.get('')
data = response.json()

"""
r = requests.get('https://bdmep.inmet.gov.br/$2a$10$mwzyjeScvWM7EvtZ3Z1ZDezZWIZTzRcbdMNULILAmfFQeNQD07LXe.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("/home/rodrigo/Dev")
"""

producer.send('dados-bdmep', json.dumps(data).encode('utf-8'))
producer.close()
