# models/__init__.py
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from database import Base
from datetime import datetime

class Category(Base):
    __tablename__ = "categories"
    MaDanhMuc = Column(String, primary_key=True, index=True)
    TenDanhMuc = Column(String, index=True)
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"
    MaSP = Column(String, primary_key=True, index=True)
    TenSP = Column(String, index=True)
    Gia = Column(Float)
    MaDanhMuc = Column(String, ForeignKey("categories.MaDanhMuc"))
    category = relationship("Category", back_populates="products")

class Order(Base):
    __tablename__ = "orders"
    MaDonHang = Column(String, primary_key=True, index=True)
    MaKhachHang = Column(String, index=True)
    NgayDat = Column(DateTime, default=datetime.utcnow)