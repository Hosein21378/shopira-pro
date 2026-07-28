from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(20))
    balance = Column(Integer, default=0)  # به تومان
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(1000))
    price = Column(Integer, nullable=False)  # تومان
    duration_days = Column(Integer)  # مدت اعتبار
    stock = Column(Integer, default=-1)  # -1 = نامحدود
    is_active = Column(Boolean, default=True)
    category = Column(String(100))  # vpn, account, digital, etc.


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    amount = Column(Integer)
    status = Column(String(20), default="pending")  # pending, paid, delivered, cancelled
    invoice_number = Column(String(50), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    paid_at = Column(DateTime)

    user = relationship("User", back_populates="orders")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer)
    gateway = Column(String(50))  # pasargad, card2card, etc.
    status = Column(String(20))
    reference_id = Column(String(100))
    invoice_number = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
