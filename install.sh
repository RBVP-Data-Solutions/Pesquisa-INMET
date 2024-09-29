#AIRFLOW
sudo rm -rf airflow;
sudo mkdir airflow;
sudo chmod 755 airflow;
cd airflow;
sudo curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.3/docker-compose.yaml';
sudo chmod 644 docker-compose.yaml;
sudo mkdir -p ./dags ./logs ./plugins ./scripts ./datasets;
sudo echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env;
sudo chmod 755 dags;
sudo chmod 755 logs;
sudo chmod 755 plugins;
sudo chmod 755 scripts;
sudo chmod 755 datasets;
cd ..

#KAFKA
sudo rm -rf kafka;
sudo mkdir kafka;
cd kafka;
sudo git clone https://github.com/confluentinc/cp-all-in-one;
cd cp-all-in-one/cp-all-in-one/;
sudo docker compose up -d
cd ..
cd ..
cd ..

# PYSPARK & SUPERSET
sudo docker compose up
