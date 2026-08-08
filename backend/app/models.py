from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Admin & staff DB (vista1.db)
class Staff(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    name: Optional[str] = None
    role: str = 'staff'  # 'staff' or 'admin'
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AdminSettings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    key: str
    value: str

# Users DB (lamaliva1.db)
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    name: Optional[str] = None
    is_verified: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

class OTP(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_email: str
    code: str
    expires_at: datetime

class Room(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price_xaf: int
    capacity: int
    description: Optional[str] = None

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    room_id: int
    checkin: datetime
    checkout: datetime
    status: str = 'reserved'
    created_at: datetime = Field(default_factory=datetime.utcnow)
    customer_id_number: Optional[str] = None

# Invoices DB (laVista.db)
class Invoice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    booking_id: int
    total_xaf: int
    vat_xaf: int
    method: str
    payment_ref: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
