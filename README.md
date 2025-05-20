# Bibliothèque Numérique - Lycée Professionnel

Ce projet est une application web de gestion et de consultation de livres numériques pour un lycée professionnel. Elle permet aux élèves, enseignants et administrateurs de consulter, télécharger, uploader et gérer les ouvrages disponibles.

## Fonctionnalités principales

* Authentification JWT (login/register)
* Attribution de rôles (admin, enseignant, élève)
* Upload de livres (PDF/EPUB)
* Recherche de livres par titre
* Dashboard admin avec statistiques utilisateurs et livres

## Technologies utilisées

* **Backend** : FastAPI, MongoDB
* **Frontend** : HTML, TailwindCSS, JavaScript Vanilla
* **Base de données** : MongoDB
* **Conteneurisation** : Docker & Docker Compose

## Installation (en local)

1. Cloner le repo

```bash
git clone https://github.com/votre-nom/bibliotheque-numerique.git
cd bibliotheque-numerique
```

2. Lancer avec Docker

```bash
docker-compose up --build
```

3. Accéder à l'application sur [http://localhost:5500](http://localhost:5500)

## Accès API (FastAPI)

* Authentification : `POST /auth/login`, `POST /auth/register`
* Upload livre : `POST /books/upload`
* Recherche : `GET /books/search?title=...`
* Stats : `GET /auth/stats`, `GET /books/count`, `GET /books/recent`

---

**DOCUMENTATION TECHNIQUE**

# Structure du projet

```
bibliotheque-numerique/
├── app/
│   ├── main.py               # Point d'entrée FastAPI
│   ├── routes/
│   │   ├── auth.py           # Routes d'authentification et stats admin
│   │   └── books.py          # Upload, recherche, téléchargement de livres
│   ├── models/
│   │   └── user.py           # Schémas Pydantic pour les utilisateurs
│   ├── core/
│   │   └── security.py       # JWT, hashage mot de passe, utilisateur courant
│   └── dependencies.py       # Connexion à MongoDB et collections
├── frontend/
│   ├── index.html            # Page d'accueil
│   ├── login.html            # Page de connexion
│   ├── register.html         # Page d'inscription
│   ├── explore.html          # Recherche & téléchargement
│   ├── upload.html           # Upload (enseignants/admins uniquement)
│   ├── dashboard.html        # Statistiques admin
│   └── navbar.js             # Navbar dynamique selon le rôle
├── Dockerfile
├── docker-compose.yml
└── README.md
```

# Modèle de données (MongoDB)

## Utilisateur (users)

```json
{
  "email": "test@example.com",
  "password": "<hashed>",
  "role": "eleve | enseignant | admin"
}
```

## Livre (books)

```json
{
  "title": "Programmation Python",
  "author": "John Doe",
  "category": "Informatique",
  "isbn": "978-123456789",
  "niveau": "BTS SIO",
  "filename": "programmation-python.pdf",
  "created_at": "2025-05-19T12:34:56"
}
```

# Flux JWT

1. Authentification via `/auth/login` → retourne `access_token`
2. Le token est stocké en `localStorage` dans le navigateur
3. Les requêtes upload ou stats utilisent `Authorization: Bearer <token>`

# Dépendances Python (requirements)

* fastapi
* pymongo
* python-multipart
* jose
* passlib\[bcrypt]
* uvicorn

# Remarques sécurité

* Le `SECRET_KEY` doit être défini via les variables d'environnement en production
* Les routes critiques sont protégées par `Depends(get_current_user)`
* Le rôle est extrait du token et contrôlé à chaque appel
