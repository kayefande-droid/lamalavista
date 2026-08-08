"""Seed script for Lamalavista backend.
Creates the three SQLite DB files and seeds an admin and sample rooms.
"""
from app.db import create_all, get_session_admin, get_session_users
from app.models import Staff, Room
from passlib.hash import bcrypt
import os
from dotenv import load_dotenv
load_dotenv()

create_all()

# Admin
s = get_session_admin()
admin_email = os.getenv('ADMIN_EMAIL', 'admin@lamalavista.local')
admin_pw_raw = os.getenv('ADMIN_MASTER_PASSWORD', 'ChangeThisAdminPW')
admin_pw_hash = bcrypt.hash(admin_pw_raw)
admin = Staff(email=admin_email, name='Administrator', role='admin', hashed_password=admin_pw_hash)
# If an admin with this email exists, skip
existing = s.query(Staff).filter(Staff.email == admin_email).first()
if not existing:
    s.add(admin)
    s.commit()

# Rooms in users DB
su = get_session_users()
rooms = [
    Room(name='Standard', price_xaf=10000, capacity=2),
    Room(name='Deluxe', price_xaf=20000, capacity=2),
    Room(name='Suite', price_xaf=40000, capacity=3),
    Room(name='Presidential Suite', price_xaf=60000, capacity=4),
]
for r in rooms:
    existing = su.query(Room).filter(Room.name == r.name).first()
    if not existing:
        su.add(r)
su.commit()
print('Seeding complete.')
