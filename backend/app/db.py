from sqlmodel import SQLModel, create_engine, Session
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMIN_DB = f"sqlite:///{os.path.join(BASE_DIR, '..', 'vista1.db')}"
USERS_DB = f"sqlite:///{os.path.join(BASE_DIR, '..', 'lamaliva1.db')}"
INVOICES_DB = f"sqlite:///{os.path.join(BASE_DIR, '..', 'laVista.db')}"

# Connect args for SQLite in single-threaded dev
engine_admin = create_engine(ADMIN_DB, connect_args={"check_same_thread": False})
engine_users = create_engine(USERS_DB, connect_args={"check_same_thread": False})
engine_invoices = create_engine(INVOICES_DB, connect_args={"check_same_thread": False})


def create_all():
    # import models to ensure they register with SQLModel metadata
    from app import models
    SQLModel.metadata.create_all(engine_admin)
    SQLModel.metadata.create_all(engine_users)
    SQLModel.metadata.create_all(engine_invoices)


def get_session_admin():
    return Session(engine_admin)


def get_session_users():
    return Session(engine_users)


def get_session_invoices():
    return Session(engine_invoices)
