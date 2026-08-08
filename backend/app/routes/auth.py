from fastapi import APIRouter, HTTPException
from app.db import get_session_users
from app.models import User, OTP
from app.schemas import SignupIn, VerifyIn
from datetime import datetime, timedelta
import random
from app.email_utils import send_email

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post('/signup')
async def signup(payload: SignupIn):
    session = get_session_users()
    user = session.query(User).filter(User.email == payload.email).first()
    if not user:
        user = User(email=payload.email, name=payload.name, is_verified=False)
        session.add(user)
        session.commit()
    # generate OTP
    code = f"{random.randint(0, 999999):06d}"
    otp = OTP(user_email=payload.email, code=code, expires_at=datetime.utcnow() + timedelta(minutes=10))
    session.add(otp)
    session.commit()
    # send email (async)
    try:
        await send_email(payload.email, subject='Lamalavista OTP', html=f"Your OTP: <strong>{code}</strong>")
    except Exception as e:
        # swallow for dev but log
        print('email send failed', e)
    return {"msg": "OTP sent to your Gmail address"}

@router.post('/verify')
def verify(payload: VerifyIn):
    session = get_session_users()
    otp = session.query(OTP).filter(OTP.user_email == payload.email, OTP.code == payload.code).order_by(OTP.id.desc()).first()
    if not otp or otp.expires_at < datetime.utcnow():
        raise HTTPException(400, 'OTP invalid or expired')
    user = session.query(User).filter(User.email == payload.email).first()
    user.is_verified = True
    session.add(user)
    session.commit()
    return {"msg": "verified"}
