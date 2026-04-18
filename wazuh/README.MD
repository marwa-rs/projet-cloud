# Wazuh - Installation et Configuration

# Composants
- Wazuh Manager qui surveille la sécurité
- Wazuh Indexer qui stocke les alertes
- Wazuh Dashboard qui interface web

## Installation Single Node Docker

# 1. Cloner la config officielle
git clone https://github.com/wazuh/wazuh-docker.git -b v4.7.0 --depth 1
cd wazuh-docker/single-node

# 2. Générer les certificats SSL
sudo docker-compose -f generate-indexer-certs.yml run --rm generator

# 3. Lancer Wazuh
sudo docker-compose up -d

## Accès Dashboard
URL: https://192.168.56.10
Username: admin
Password: SecretPassword

## Installation Agent
sudo WAZUH_MANAGER='172.17.0.1' WAZUH_AGENT_NAME='projet-cloud-vm' dpkg -i wazuh-agent_4.7.0-1_amd64.deb
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
