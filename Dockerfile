# 1. On part d'une image Linux officielle très légère qui contient déjà Python
FROM python:3.11-slim

# 2. On définit le dossier de travail à l'intérieur du conteneur
WORKDIR /workdir

# 3. On copie le fichier des dépendances dans le conteneur
COPY app/requirements.txt .

# 4. On installe les dépendances requises (Flask et le client Prometheus)
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le reste du code de notre application
COPY app/ .

# 6. On indique que l'application va utiliser le port 5000
EXPOSE 5000

# 7. La commande pour démarrer l'application quand le conteneur s'allume
CMD ["python", "main.py"]