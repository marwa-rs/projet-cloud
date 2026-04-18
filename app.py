# Wazuh - Installation et Configuration

## Composants
from flask import Flask, render_template_string
import subprocess
import datetime

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projet Cloud - Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #0a0e1a;
            color: #e0e6f0;
            min-height: 100vh;
        }
        header {
            background: linear-gradient(135deg, #1a1f3a, #0d1117);
            padding: 20px 40px;
            border-bottom: 2px solid #00d4ff;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header h1 {
            font-size: 24px;
            color: #00d4ff;
            letter-spacing: 2px;
        }
        header span {
            color: #888;
            font-size: 14px;
        }
        .hero {
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(180deg, #0d1117, #0a0e1a);
        }
        .hero h2 {
            font-size: 48px;
            color: #00d4ff;
            margin-bottom: 15px;
        }
        .hero p {
            font-size: 18px;
            color: #888;
            max-width: 600px;
            margin: 0 auto 30px;
        }
        .badge {
            display: inline-block;
            padding: 8px 20px;
            border-radius: 20px;
            margin: 5px;
            font-size: 13px;
            font-weight: bold;
        }
        .badge-blue { background: #1a3a5c; color: #00d4ff; border: 1px solid #00d4ff; }
        .badge-green { background: #1a3a2a; color: #00ff88; border: 1px solid #00ff88; }
        .badge-purple { background: #2a1a3a; color: #b088ff; border: 1px solid #b088ff; }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            margin-bottom: 40px;
        }
        .card {
            background: #1a1f3a;
            border-radius: 12px;
            border: 1px solid #2a3050;
            transition: transform 0.3s, border-color 0.3s;
        }
        .card:hover {
            border-color: #00d4ff;
        }
        .card-header {
            display: flex;
            margin-bottom: 15px;
        }
        .card-icon {
            width: 45px;
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
        }
        .icon-blue { background: #1a3a5c; }
        .icon-green { background: #1a3a2a; }
        .icon-purple { background: #2a1a3a; }
        .card h3 { font-size: 18px; color: #e0e6f0; }
        .card p { color: #888; font-size: 14px; margin-top: 5px; }
            width: 10px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        .dot-red { background: #ff4444; box-shadow: 0 0 8px #ff4444; }
        .service-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #2a3050;
        }
        .service-item:last-child { border-bottom: none; }
        .service-name { font-size: 14px; color: #ccc; }
        .service-port { font-size: 12px; color: #888; }
        .status-active {
            background: #1a3a2a;
            color: #00ff88;
            padding: 3px 10px;
            border-radius: 10px;
            font-size: 12px;
        }
        .links {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .link-btn {
            display: inline-block;
            padding: 10px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 14px;
            font-weight: bold;
            transition: opacity 0.3s;
        }
        .link-btn:hover { opacity: 0.8; }
        .btn-blue { background: #00d4ff; color: #0a0e1a; }
        .btn-green { background: #00ff88; color: #0a0e1a; }
        .btn-purple { background: #b088ff; color: #0a0e1a; }
        .btn-orange { background: #ff8800; color: #0a0e1a; }
        footer {
            text-align: center;
            padding: 30px;
            color: #888;
            border-top: 1px solid #2a3050;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <header>
        <h1>🚀 PROJET CLOUD</h1>
                            <span class="status-dot dot-green"></span>Pipeline actif
                        </span>
                    <div class="service-item">
                        <span class="service-port">toutes les 2 min</span>
                        <span class="service-port">:8080</span>
                    </div>
                <div class="links">
                    <a href="http://192.168.56.10:8080" class="link-btn btn-green" target="_blank">Ouvrir Jenkins</a>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <div class="card-icon icon-red">🛡️</div>
                    <div>
                        <h3>Wazuh Security</h3>
                        <p>IDS & Monitoring</p>
                    </div>
                </div>
                <div class="service-list">
                    <div class="service-item">
                        <span class="service-name">
                            <span class="status-dot dot-green"></span>Agent actif
                        </span>
                        <span class="status-active">✅ Running</span>
                    </div>
                    <div class="service-item">
                        <span class="service-name">Agent</span>
                        <span class="service-port">projet-cloud-vm</span>
                    </div>
                    <div class="service-item">
                        <span class="service-name">Port</span>
                        <span class="service-port">:443</span>
                    </div>
                </div>
                <div class="links">
                    <a href="https://192.168.56.10" class="link-btn btn-orange" target="_blank">Ouvrir Wazuh</a>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <div class="card-icon icon-orange">📊</div>
                    <div>
                        <h3>Grafana</h3>
                        <p>Dashboard supervision</p>
                    </div>
                </div>
                <div class="service-list">
                    <div class="service-item">
                        <span class="service-name">
                            <span class="status-dot dot-green"></span>Dashboard actif
                        </span>
                        <span class="status-active">✅ Running</span>
                    </div>
                    <div class="service-item">
                        <span class="service-name">Prometheus</span>
                        <span class="service-port">:9090</span>
                    </div>
                    <div class="service-item">
                        <span class="service-name">Port</span>
                        <span class="service-port">:3000</span>
                    </div>
                </div>
                <div class="links">
                    <a href="http://192.168.56.10:3000" class="link-btn btn-purple" target="_blank">Ouvrir Grafana</a>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <div class="card-icon icon-blue">🐳</div>
                    <div>
                        <h3>Infrastructure</h3>
                        <p>Vagrant + VirtualBox</p>
                    </div>
                </div>
                <div class="service-list">
                    <div class="service-item">
                        <span class="service-name">OS</span>
                        <span class="service-port">Ubuntu 22.04 LTS</span>
                    </div>
                    <div class="service-item">
                        <span class="service-name">IP</span>
                        <span class="service-port">192.168.56.10</span>
                    </div>
                    <div class="service-item">
                        <span class="service-name">RAM</span>
                        <span class="service-port">5GB</span>
                    </div>
                </div>
            </div>

        </div>

        <div class="card">
            <div class="card-header">
                <div class="card-icon icon-purple">🏗️</div>
                <div>
                    <h3>Stack Technique</h3>
                    <p>Technologies utilisées dans ce projet</p>
                </div>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
                <span class="badge badge-blue">Vagrant 2.4.9</span>
                <span class="badge badge-green">Docker 29.1.3</span>
                <span class="badge badge-purple">Jenkins 2.555</span>
                <span class="badge badge-blue">Wazuh 4.7.0</span>
                <span class="badge badge-green">Grafana Latest</span>
                <span class="badge badge-purple">Prometheus Latest</span>
                <span class="badge badge-blue">Python 3.11</span>
                <span class="badge badge-green">Flask 3.1.3</span>
                <span class="badge badge-purple">Ubuntu 22.04</span>
            </div>
        </div>

    </div>

    <footer>
        <p>🎓 Projet réalisé dans le cadre de la formation Réseau Systèmes Services Programmables — 2025</p>
        <p style="margin-top: 10px; color: #555;">Plateforme Cloud Sécurisée avec DevOps et Supervision Réseau</p>
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template_string(HTML, datetime=now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)                </div>
                    <div class="service-item">
                        <span class="service-name">Port</span>
                    </div>
                        <span class="service-name">Polling GitHub</span>
                        <span class="status-active">✅ Running</span>
                    </div>
                <div class="service-list">
                    <div class="service-item">
                        <span class="service-name">
        <span>{{ datetime }}</span>
    </header>

    <div class="hero">
        <h2>Plateforme Cloud Sécurisée</h2>
        <p>Infrastructure DevOps complète avec CI/CD, sécurité et supervision en temps réel</p>
        <div>
            <span class="badge badge-blue">🐳 Docker</span>
                </div>
                    </div>
        <div class="grid">
                        <p>Pipeline automatisé</p>
                        <h3>Jenkins CI/CD</h3>
                    <div>

                    <div class="card-icon icon-green">⚙️</div>
                <div class="card-header">
            <div class="card">
    <div class="container">

            <span class="badge badge-green">⚙️ Jenkins</span>
            <span class="badge badge-purple">🛡️ Wazuh</span>
            <span class="badge badge-blue">📊 Grafana</span>
            <span class="badge badge-green">🐍 Python/Flask</span>
            <span class="badge badge-purple">📦 Vagrant</span>
        </div>
    </div>
        .service-list { margin-top: 15px; }
        .dot-green { background: #00ff88; box-shadow: 0 0 8px #00ff88; }
            height: 10px;
        .status-dot {
        .icon-orange { background: #3a2a1a; }
        .icon-red { background: #3a1a1a; }
            font-size: 22px;
            border-radius: 10px;
            align-items: center;
            transform: translateY(-5px);
            padding: 25px;

