from fastapi import APIRouter, HTTPException
from app.db import get_session_admin
from app.models import AdminSettings
import os

router = APIRouter(prefix="/admin/payments", tags=["payments"])

@router.post('/config')
def set_payment_config(payload: dict, admin_password: str):
    # Very small demo validation: compare provided admin_password to env var (do not store plaintext in prod)
    master_hash = os.getenv('ADMIN_MASTER_PASSWORD_HASH')
    if not master_hash:
        raise HTTPException(500, 'Admin password not configured')
    # TODO: verify hash properly (bcrypt). Here we accept any for demo
    session = get_session_admin()
    for k, v in payload.items():
        s = session.query(AdminSettings).filter(AdminSettings.key == k).first()
        if s:
            s.value = v
        else:
            s = AdminSettings(key=k, value=v)
            session.add(s)
    session.commit()
    return {'msg': 'payment settings saved'}

@router.get('/links')
def get_payment_links():
    return {
        'momo_developer': 'https://momodeveloper.mtn.com',
        'flutterwave': 'https://flutterwave.com',
        'paystack': 'https://paystack.com',
        'stripe': 'https://stripe.com'
    }
