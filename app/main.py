import time
import random
from flask import Flask, Response
from prometheus_client import generate_latest, Counter

app = Flask(__name__)

# Ici, on crée un "Compteur" Prometheus. Il va compter le nombre de clics sur notre site.
COMPTEUR_REQUETES = Counter(
    'nombre_total_de_visites', 
    'Compte le nombre total de visiteurs sur l application'
)

@app.route('/')
def home():
    # À chaque fois qu'un utilisateur visite cette page, on augmente le compteur de 1
    COMPTEUR_REQUETES.inc()
    
    # On simule un petit temps de chargement aléatoire
    time.sleep(random.uniform(0.1, 0.4))
    
    return {"statut": "En ligne", "message": "Bienvenue sur notre application professionnelle !"}, 200

@app.route('/metrics')
def metrics():
    # C'est la page secrète que notre outil de surveillance va lire pour récupérer les statistiques
    return Response(generate_latest(), mimetype='text/plain; version=0.0.4; charset=utf-8')

if __name__ == '__main__':
    # L'application écoute sur le port 5000
    app.run(host='0.0.0.0', port=5000)