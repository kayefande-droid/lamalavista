# Lamalavista — Hotel platform (FastAPI + React PWA)

An installable, offline-capable hotel booking & staff/admin platform inspired by La Maliva Vista Hotel (Buea, Cameroon).

This branch contains a full-stack scaffold ready for development and deploy on Render. It includes:

- frontend: React 18 PWA (frontend/)
- backend: FastAPI app with multi-DB routing (backend/)
- Seed data and scripts to initialize three local SQLite DBs for quick testing
- Deployment tips and sample render.yaml

Important: For production, move from SQLite to PostgreSQL and keep secrets out of the repo (use Render environment variables or a secret manager).

Quick start (development)

1. Backend

   cd backend
   python -m venv .venv
   source .venv/bin/activate     # Windows: .\.venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env to configure SMTP and admin password before seeding
   python seed.py
   uvicorn app.main:app --reload --port 8000

2. Frontend

   cd frontend
   npm install
   npm start

3. Production build (single-host approach)

   # Build frontend and let backend serve the static build
   cd frontend && npm ci && npm run build
   cp -R build ../backend/frontend_build
   cd ../backend
   # Set environment variables and run gunicorn in production
   gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT --workers 4

Render notes

- Recommended: create two Render services (Backend web service + Frontend static site)
- Use Render Postgres for production databases and set ADMIN_DATABASE_URL, USERS_DATABASE_URL, INVOICES_DATABASE_URL as env vars
- Store SMTP and payment credentials in Render environment configuration

For more details see backend/README.md and docs/payment-integration.md
