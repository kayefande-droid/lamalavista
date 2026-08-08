from pydantic import BaseModel, EmailStr
from typing import Optional

class SignupIn(BaseModel):
    email: EmailStr
    name: str

class VerifyIn(BaseModel):
    email: EmailStr
    code: str
