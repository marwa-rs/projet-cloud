# -*- coding: utf-8 -*-
from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projet Cloud - Plateforme DevOps</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #0a0e1a; color: #e0e6f0; }

        /* NAV */
        nav {
            background: #0d1117;
            padding: 15px 40px;
            border-bottom: 1px solid #2a3050;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        nav .logo { color: #00d4ff; font-size: 20px; font-weight: bold; letter-spacing: 2px; }
        nav ul { list-style: none; display: flex; gap: 30px; }
        nav ul li a { color: #888; text-decoration: none; font-size: 14px; transition: color 0.3s; }
        nav ul li a:hover { color: #00d4ff; }

        /* HERO */
        .hero {
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(180deg, #0d1117 0%, #0a0e1a 100%);
            border-bottom: 1px solid #2a3050;
        }
        .hero h1 { font-size: 52px; color: #00d4ff; margin-bottom: 15px; letter-spacing: 3px; }
        .hero p { font-size: 18px; color: #888; max-width: 700px; margin: 0 auto 30px; line-height: 1.6; }
        .badges { margin-top: 20px; }
        .badge { display: inline-block; padding: 6px 18px; border-radius: 20px; margin: 5px; font-size: 13px; font-weight: bold; }
        .badge-blue { background: #1a3a5c; color: #00d4ff; border: 1px solid #00d4ff; }
        .badge-green { background: #1a3a2a; color: #00ff88; border: 1px solid #00ff88; }
        .badge-purple { background: #2a1a3a; color: #b088ff; border: 1px solid #b088ff; }
        .badge-orange { background: #3a2a1a; color: #ff8800; border: 1px solid #ff8800; }

        /* STATS */
        .stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            padding: 40px 20px;
            background: #0d1117;
            border-bottom: 1px solid #2a3050;
            flex-wrap: wrap;
        }
        .stat-item { text-align: center; }
        .stat-number { font-size: 42px; font-weight: bold; color: #00d4ff; }
        .stat-label { font-size: 14px; color: #888; margin-top: 5px; }

        /* SECTIONS */
        .section { padding: 60px 40px; max-width: 1200px; margin: 0 auto; }
        .section-title {
            font-size: 28px;
            color: #00d4ff;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 1px solid #2a3050;
        }

        /* CARDS SERVICES */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; }
        .card {
            background: #1a1f3a;
            border-radius: 12px;
            padding: 25px;
            border: 1px solid #2a3050;
            transition: transform 0.3s, border-color 0.3s;
        }
        .card:hover { transform: translateY(-5px); border-color: #00d4ff; }
        .card-top { display: flex; align-items: center; margin-bottom: 15px; }
        .card-icon { font-size: 32px; margin-right: 15px; }
        .card h3 { font-size: 18px; color: #e0e6f0; }
        .card .version { font-size: 12px; color: #00ff88; margin-top: 3px; }
        .card-info { margin-top: 15px; }
        .info-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #2a3050; font-size: 14px; }
        .info-row:last-child { border-bottom: none; }
        .info-key { color: #888; }
        .info-val { color: #e0e6f0; }
        .dot { width: 8px; height: 8px; border-radius: 50%; background: #00ff88; display: inline-block; margin-right: 6px; box-shadow: 0 0 6px #00ff88; }
        .btn { display: inline-block; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 15px; font-size: 14px; transition: opacity 0.3s; }
        .btn:hover { opacity: 0.8; }
        .btn-green { background: #00ff88; color: #0a0e1a; }
        .btn-orange { background: #ff8800; color: #0a0e1a; }
        .btn-purple { background: #b088ff; color: #0a0e1a; }
        .btn-blue { background: #00d4ff; color: #0a0e1a; }

        /* ARCHITECTURE */
        .arch-box {
            background: #1a1f3a;
            border-radius: 12px;
            padding: 40px;
            border: 1px solid #2a3050;
            text-align: center;
        }
        .arch-flow {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
        }
        .arch-node {
            background: #0d1117;
            border: 2px solid #00d4ff;
            border-radius: 10px;
            padding: 15px 20px;
            min-width: 120px;
            text-align: center;
        }
        .arch-node .icon { font-size: 24px; margin-bottom: 8px; }
        .arch-node .name { font-size: 13px; color: #00d4ff; font-weight: bold; }
        .arch-node .port { font-size: 11px; color: #888; margin-top: 4px; }
        .arch-arrow { color: #00d4ff; font-size: 24px; font-weight: bold; }
        .arch-node-green { border-color: #00ff88; }
        .arch-node-green .name { color: #00ff88; }
        .arch-node-orange { border-color: #ff8800; }
        .arch-node-orange .name { color: #ff8800; }
        .arch-node-purple { border-color: #b088ff; }
        .arch-node-purple .name { color: #b088ff; }

        /* STACK */
        .stack-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
        .stack-item {
            background: #1a1f3a;
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #2a3050;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .stack-icon { font-size: 28px; }
        .stack-name { font-size: 15px; font-weight: bold; color: #e0e6f0; }
        .stack-version { font-size: 12px; color: #00ff88; margin-top: 3px; }
        .stack-role { font-size: 12px; color: #888; margin-top: 2px; }

        /* PIPELINE */
        .pipeline {
            background: #1a1f3a;
            border-radius: 12px;
            padding: 30px;
            border: 1px solid #2a3050;
        }
        .pipeline-steps {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }
        .pipeline-step {
            background: #0d1117;
            border: 1px solid #2a3050;
            border-radius: 8px;
            padding: 12px 20px;
            text-align: center;
            min-width: 110px;
        }
        .step-num { font-size: 11px; color: #888; }
        .step-name { font-size: 14px; color: #00d4ff; font-weight: bold; margin-top: 4px; }
        .step-desc { font-size: 11px; color: #888; margin-top: 3px; }
        .pipeline-arrow { color: #00d4ff; font-size: 20px; }

        /* FOOTER */
        footer {
            background: #0d1117;
            border-top: 1px solid #2a3050;
            padding: 30px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }
        footer .footer-left h3 { color: #00d4ff; margin-bottom: 5px; }
        footer .footer-left p { color: #888; font-size: 13px; }
        footer .footer-right { text-align: right; }
        footer .footer-right p { color: #888; font-size: 13px; }
    </style>
</head>
<body>

    <!-- NAVIGATION -->
    <nav>
        <div class="logo">PROJET CLOUD</div>
        <ul>
            <li><a href="#services">Services</a></li>
            <li><a href="#architecture">Architecture</a></li>
            <li><a href="#stack">Stack</a></li>
            <li><a href="#pipeline">Pipeline</a></li>
        </ul>
    </nav>

    <!-- HERO -->
    <div class="hero">
        <h1>Plateforme Cloud Securisee</h1>
        <p>Infrastructure DevOps complete integrant CI/CD automatise, detection d'intrusion en temps reel et supervision centralisee</p>
        <div class="badges">
            <span class="badge badge-blue">Docker</span>
            <span class="badge badge-green">Jenkins</span>
            <span class="badge badge-purple">Wazuh</span>
            <span class="badge badge-orange">Grafana</span>
            <span class="badge badge-blue">Flask</span>
            <span class="badge badge-green">Vagrant</span>
            <span class="badge badge-purple">Prometheus</span>
            <span class="badge badge-orange">Ubuntu</span>
        </div>
    </div>

    <!-- STATS -->
    <div class="stats">
        <div class="stat-item">
            <div class="stat-number">8</div>
            <div class="stat-label">Services actifs</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1</div>
            <div class="stat-label">VM Ubuntu</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">5</div>
            <div class="stat-label">Ports exposes</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">5GB</div>
            <div class="stat-label">RAM allouee</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">2min</div>
            <div class="stat-label">Deploy auto</div>
        </div>
    </div>

    <!-- SERVICES -->
    <div class="section" id="services">
        <h2 class="section-title">Services</h2>
        <div class="grid">

            <div class="card">
                <div class="card-top">
                    <div class="card-icon">Jenkins</div>
                    <div>
                        <h3>Jenkins CI/CD</h3>
                        <div class="version">v2.555.1</div>
                    </div>
                </div>
                <div class="card-info">
                    <div class="info-row">
                        <span class="info-key">Statut</span>
                        <span class="info-val"><span class="dot"></span>Actif</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Port</span>
                        <span class="info-val">:8080</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Polling</span>
                        <span class="info-val">2 minutes</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Source</span>
                        <span class="info-val">GitHub</span>
                    </div>
                </div>
                <a href="http://192.168.56.10:8080" class="btn btn-green" target="_blank">Ouvrir Jenkins</a>
            </div>

            <div class="card">
                <div class="card-top">
                    <div class="card-icon">Wazuh</div>
                    <div>
                        <h3>Wazuh Security</h3>
                        <div class="version">v4.7.0</div>
                    </div>
                </div>
                <div class="card-info">
                    <div class="info-row">
                        <span class="info-key">Statut</span>
                        <span class="info-val"><span class="dot"></span>Actif</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Port</span>
                        <span class="info-val">:443</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Agent</span>
                        <span class="info-val">projet-cloud-vm</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Type</span>
                        <span class="info-val">IDS / SIEM</span>
                    </div>
                </div>
                <a href="https://192.168.56.10" class="btn btn-orange" target="_blank">Ouvrir Wazuh</a>
            </div>

            <div class="card">
                <div class="card-top">
                    <div class="card-icon">Grafana</div>
                    <div>
                        <h3>Grafana</h3>
                        <div class="version">Latest</div>
                    </div>
                </div>
                <div class="card-info">
                    <div class="info-row">
                        <span class="info-key">Statut</span>
                        <span class="info-val"><span class="dot"></span>Actif</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Port</span>
                        <span class="info-val">:3000</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Source</span>
                        <span class="info-val">Prometheus</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Dashboard</span>
                        <span class="info-val">Node Exporter Full</span>
                    </div>
                </div>
                <a href="http://192.168.56.10:3000" class="btn btn-purple" target="_blank">Ouvrir Grafana</a>
            </div>

            <div class="card">
                <div class="card-top">
                    <div class="card-icon">VM</div>
                    <div>
                        <h3>Infrastructure</h3>
                        <div class="version">Ubuntu 22.04 LTS</div>
                    </div>
                </div>
                <div class="card-info">
                    <div class="info-row">
                        <span class="info-key">IP</span>
                        <span class="info-val">192.168.56.10</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">RAM</span>
                        <span class="info-val">5 GB</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">CPU</span>
                        <span class="info-val">2 vCPU</span>
                    </div>
                    <div class="info-row">
                        <span class="info-key">Provider</span>
                        <span class="info-val">VirtualBox</span>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <!-- ARCHITECTURE -->
    <div class="section" id="architecture">
        <h2 class="section-title">Architecture</h2>
        <div class="arch-box">
            <p style="color: #888; margin-bottom: 30px;">Flux de deploiement et supervision de l'infrastructure</p>

            <div class="arch-flow">
                <div class="arch-node">
                    <div class="icon">Dev</div>
                    <div class="name">GitHub</div>
                    <div class="port">git push</div>
                </div>
                <div class="arch-arrow">→</div>
                <div class="arch-node arch-node-green">
                    <div class="icon">CI</div>
                    <div class="name">Jenkins</div>
                    <div class="port">:8080</div>
                </div>
                <div class="arch-arrow">→</div>
                <div class="arch-node arch-node-purple">
                    <div class="icon">App</div>
                    <div class="name">Docker</div>
                    <div class="port">:5000</div>
                </div>
            </div>

            <div style="margin: 20px 0; color: #2a3050; font-size: 20px;">↓ surveillance</div>

            <div class="arch-flow">
                <div class="arch-node arch-node-orange">
                    <div class="icon">IDS</div>
                    <div class="name">Wazuh</div>
                    <div class="port">:443</div>
                </div>
                <div class="arch-arrow">+</div>
                <div class="arch-node arch-node-purple">
                    <div class="icon">Met</div>
                    <div class="name">Prometheus</div>
                    <div class="port">:9090</div>
                </div>
                <div class="arch-arrow">→</div>
                <div class="arch-node">
                    <div class="icon">Dash</div>
                    <div class="name">Grafana</div>
                    <div class="port">:3000</div>
                </div>
            </div>
        </div>
    </div>

    <!-- STACK TECHNIQUE -->
    <div class="section" id="stack">
        <h2 class="section-title">Stack Technique</h2>
        <div class="stack-grid">
            <div class="stack-item">
                <div class="stack-icon">Vag</div>
                <div>
                    <div class="stack-name">Vagrant</div>
                    <div class="stack-version">v2.4.9</div>
                    <div class="stack-role">Gestion des VMs</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">VB</div>
                <div>
                    <div class="stack-name">VirtualBox</div>
                    <div class="stack-version">v7.1</div>
                    <div class="stack-role">Hyperviseur</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Doc</div>
                <div>
                    <div class="stack-name">Docker</div>
                    <div class="stack-version">v29.1.3</div>
                    <div class="stack-role">Conteneurisation</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Jen</div>
                <div>
                    <div class="stack-name">Jenkins</div>
                    <div class="stack-version">v2.555.1</div>
                    <div class="stack-role">CI/CD Pipeline</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Py</div>
                <div>
                    <div class="stack-name">Python</div>
                    <div class="stack-version">v3.11</div>
                    <div class="stack-role">Langage backend</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Fla</div>
                <div>
                    <div class="stack-name">Flask</div>
                    <div class="stack-version">v3.1.3</div>
                    <div class="stack-role">Framework web</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Waz</div>
                <div>
                    <div class="stack-name">Wazuh</div>
                    <div class="stack-version">v4.7.0</div>
                    <div class="stack-role">IDS / SIEM</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Gra</div>
                <div>
                    <div class="stack-name">Grafana</div>
                    <div class="stack-version">Latest</div>
                    <div class="stack-role">Supervision</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Pro</div>
                <div>
                    <div class="stack-name">Prometheus</div>
                    <div class="stack-version">v3.11.2</div>
                    <div class="stack-role">Metriques</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Git</div>
                <div>
                    <div class="stack-name">GitHub</div>
                    <div class="stack-version">-</div>
                    <div class="stack-role">Source control</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">Ubu</div>
                <div>
                    <div class="stack-name">Ubuntu</div>
                    <div class="stack-version">22.04 LTS</div>
                    <div class="stack-role">Systeme d'exploitation</div>
                </div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">NE</div>
                <div>
                    <div class="stack-name">Node Exporter</div>
                    <div class="stack-version">Latest</div>
                    <div class="stack-role">Agent metriques</div>
                </div>
            </div>
        </div>
    </div>

    <!-- PIPELINE -->
    <div class="section" id="pipeline">
        <h2 class="section-title">Pipeline CI/CD</h2>
        <div class="pipeline">
            <p style="color: #888;">Flux automatique declenche a chaque git push</p>
            <div class="pipeline-steps">
                <div class="pipeline-step">
                    <div class="step-num">01</div>
                    <div class="step-name">Push</div>
                    <div class="step-desc">git push GitHub</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step">
                    <div class="step-num">02</div>
                    <div class="step-name">Detect</div>
                    <div class="step-desc">Jenkins polling</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step">
                    <div class="step-num">03</div>
                    <div class="step-name">Clone</div>
                    <div class="step-desc">Git checkout</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step">
                    <div class="step-num">04</div>
                    <div class="step-name">Build</div>
                    <div class="step-desc">Docker build</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step">
                    <div class="step-num">05</div>
                    <div class="step-name">Deploy</div>
                    <div class="step-desc">Docker run</div>
                </div>
                <div class="pipeline-arrow">→</div>
                <div class="pipeline-step">
                    <div class="step-num">06</div>
                    <div class="step-name">Live</div>
                    <div class="step-desc">App sur :5000</div>
                </div>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer>
        <div class="footer-left">
            <h3>Plateforme Cloud Securisee</h3>
            <p>DevOps | Securite | Supervision | CI/CD</p>
        </div>
        <div class="footer-right">
            <p>Infrastructure locale → Migration AWS</p>
            <p style="margin-top: 5px; color: #555;">IP : 192.168.56.10</p>
        </div>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)