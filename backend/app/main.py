from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title='Lamalavista Backend')

# CORS for local dev; in production set exact origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('FRONTEND_URL', 'http://localhost:3000')],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Import routers
from app.routes import auth as auth_router
from app.routes import monitor as monitor_router
from app.routes import payments as payments_router

app.include_router(auth_router.router)
app.include_router(monitor_router.router)
app.include_router(payments_router.router)

# Serve frontend build if present
frontend_build = os.path.join(os.path.dirname(__file__), '..', 'frontend_build')
if os.path.isdir(frontend_build):
    app.mount('/', StaticFiles(directory=frontend_build, html=True), name='frontend')

@app.get('/ping')
async def ping():
    return {'msg': 'pong'}
