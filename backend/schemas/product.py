from pydantic import BaseModel

class ProductBase(BaseModel):
    MaSP: str
    TenSP: str
    Gia: float
    MaDanhMuc: str

class Product(ProductBase):
    class Config:
        from_attributes = True
