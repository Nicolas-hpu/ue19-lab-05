# Utilise une image de base avec Python
FROM python:3.11-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /usr/src/app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
COPY app.py ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande par défaut pour exécuter le script
CMD ["python", "app.py"]