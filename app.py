# -*- coding: utf-8 -*-
from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Projet Cloud</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0a0e1a; color: #e0e6f0; margin: 0; }
        header { background: #1a1f3a; padding: 20px 40px; border-bottom: 2px solid #00d4ff; display: flex; justify-content: space-between; }
        header h1 { color: #00d4ff; }
        header span { color: #888; }
        .hero { text-align: center; padding: 60px 20px; }
        .hero h2 { font-size: 42px; color: #00d4ff; margin-bottom: 15px; }
        .hero p { color: #888; font-size: 18px; }
        .container { max-width: 1200px; margin: 0 auto; padding: 40px 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .card { background: #1a1f3a; border-radius: 12px; padding: 25px; border: 1px solid #2a3050; }
        .card:hover { border-color: #00d4ff; }
        .card h3 { color: #00d4ff; margin-bottom: 10px; }
        .card p { color: #888; font-size: 14px; }
        .badge { display: inline-block; padding: 5px 15px; border-radius: 15px; margin: 5px; font-size: 13px; }
        .badge-blue { background: #1a3a5c; color: #00d4ff; border: 1px solid #00d4ff; }
        .badge-green { background: #1a3a2a; color: #00ff88; border: 1px solid #00ff88; }
        .badge-purple { background: #2a1a3a; color: #b088ff; border: 1px solid #b088ff; }
        .btn { display: inline-block; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 15px; }
        .btn-blue { background: #00d4ff; color: #0a0e1a; }
        .btn-green { background: #00ff88; color: #0a0e1a; }
        .btn-orange { background: #ff8800; color: #0a0e1a; }
        .btn-purple { background: #b088ff; color: #0a0e1a; }
        .dot { width: 10px; height: 10px; border-radius: 50%; background: #00ff88; display: inline-block; margin-right: 8px; box-shadow: 0 0 8px #00ff88; }
        footer { text-align: center; padding: 30px; color: #888; border-top: 1px solid #2a3050; margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <h1>Projet Cloud</h1>
        <span>{{ datetime }}</span>
    </header>
    <div class="hero">
        <h2>Plateforme Cloud Securisee</h2>
        <p>Infrastructure DevOps avec CI/CD, securite et supervision en temps reel</p>
        <br>
        <span class="badge badge-blue">Docker</span>
        <span class="badge badge-green">Jenkins</span>
        <span class="badge badge-purple">Wazuh</span>
        <span class="badge badge-blue">Grafana</span>
        <span class="badge badge-green">Flask</span>
        <span class="badge badge-purple">Vagrant</span>
    </div>
    <div class="container">
        <div class="grid">
            <div class="card">
                <h3>Jenkins CI/CD</h3>
                <p><span class="dot"></span>Pipeline automatise</p>
                <p>Polling GitHub toutes les 2 minutes</p>
                <p>Port : 8080</p>
                <a href="http://192.168.56.10:8080" class="btn btn-green" target="_blank">Ouvrir Jenkins</a>
            </div>
            <div class="card">
                <h3>Wazuh Security</h3>
                <p><span class="dot"></span>Agent actif : projet-cloud-vm</p>
                <p>IDS et monitoring en temps reel</p>
                <p>Port : 443</p>
                <a href="https://192.168.56.10" class="btn btn-orange" target="_blank">Ouvrir Wazuh</a>
            </div>
            <div class="card">
                <h3>Grafana Dashboard</h3>
                <p><span class="dot"></span>Metriques en temps reel</p>
                <p>CPU, RAM, Reseau, Disque</p>
                <p>Port : 3000</p>
                <a href="http://192.168.56.10:3000" class="btn btn-purple" target="_blank">Ouvrir Grafana</a>
            </div>
            <div class="card">
                <h3>Infrastructure</h3>
                <p>OS : Ubuntu 22.04 LTS</p>
                <p>IP : 192.168.56.10</p>
                <p>RAM : 5GB | CPU : 2</p>
            </div>
        </div>
    </div>
    <footer>
        <p>Formation Reseau Systemes Services Programmables 2025</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template_string(HTML, datetime=now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
