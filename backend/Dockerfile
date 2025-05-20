# Utilise une image officielle Python
FROM python:3.11

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Copie tout le contenu dans le conteneur
COPY . .

# Installe les dépendances
RUN pip install fastapi uvicorn pymongo python-decouple python-jose python-multipart pydantic[email] passlib[bcrypt]


# Expose le port 8000 pour l’API
EXPOSE 8000

# Commande pour démarrer l’application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
