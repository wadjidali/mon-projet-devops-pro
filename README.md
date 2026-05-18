# 🚀 Projet d'Observabilité Multi-Conteneurs (Flask + Prometheus + Grafana)

Ce projet personnel démontre la mise en place d'une infrastructure d'observabilité moderne et conteneurisée, respectant les standards du marché DevOps. Il orchestre une application Python, un serveur de collecte de métriques et un tableau de bord visuel, le tout automatisé par une pipeline CI/CD.

---

## 🛠️ Architecture du Projet

L'infrastructure est entièrement isolée et orchestrée à l'aide de **Docker Compose** :
1. **Application Web (Flask) :** Une application Python qui expose des métriques personnalisées (compteur de visites textuelles) sur l'endpoint `/metrics`.
2. **Prometheus :** Un serveur de surveillance configuré pour scraper (collecter) les métriques de l'application toutes les 5 secondes via le réseau interne Docker.
3. **Grafana :** Un outil de visualisation connecté à Prometheus pour afficher l'évolution du trafic en temps réel.

---

## 📸 Aperçu du Projet

### 1. Lancement des conteneurs isolés
L'application s'exécute de manière fluide dans son environnement Docker :
![Terminal Flask](./images/terminal)

### 2. Statut des cibles Prometheus
Grâce à une configuration réseau Docker stricte, Prometheus détecte et interroge l'application avec succès (Statut **UP / VERT**) :
![Prometheus Targets](./images/prometheuspro)

### 3. Tableau de bord Grafana
Visualisation en temps réel de la métrique personnalisée `nombre_total_de_visites_total` lors des rafraîchissements de page :
![Grafana Dashboard](./images/grafanapro)

---

## 🚀 Pipeline CI/CD (GitHub Actions)

Le projet intègre une pipeline d'intégration continue moderne définie dans `.github/workflows/ci.yml`. À chaque modification du code (`git push`), les serveurs GitHub exécutent automatiquement :
- Une analyse syntaxique et de qualité du code Python (via `flake8`).
- Un test de construction complet de l'image Docker pour garantir la stabilité avant tout déploiement.

---

## ⚙️ Comment lancer le projet en local ?

### Prérequis
- Docker et le plugin Docker Compose installés (ou WSL2 sous Windows).

### Lancement
1. Clonez ce dépôt sur votre machine.
2. Exécutez la commande magique pour compiler et démarrer tous les services :
   ```bash
   sudo docker compose up --build
