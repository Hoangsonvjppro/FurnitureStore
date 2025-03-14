from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Product  # Sửa dòng này
from schemas.product import Product as ProductSchema

router = APIRouter()

@router.get("/products", response_model=list[ProductSchema])
async def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@router.get("/products/{ma_sp}", response_model=ProductSchema)
async def get_product(ma_sp: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.MaSP == ma_sp).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product