# Backend README

This folder contains the FastAPI backend for Lamalavista. It is intentionally simple so you can iterate quickly.

Key commands

- Install: pip install -r requirements.txt
- Seed DBs: python seed.py
- Run dev server: uvicorn app.main:app --reload --port 8000

Production

- Use Gunicorn + Uvicorn workers in production
- Use Postgres for DBs (update backend/app/db.py to read DATABASE_URLs)
- Serve frontend build using StaticFiles (copy build to backend/frontend_build or run frontend as a separate static site)

Environment variables

See .env.example for keys to set (SMTP, ADMIN_MASTER_PASSWORD_HASH, MOMO_*).
