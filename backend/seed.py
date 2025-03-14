from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Product, Category  # Sửa dòng này

# Tạo bảng
Base.metadata.create_all(bind=engine)

# Thêm dữ liệu mẫu
db = SessionLocal()

# Thêm danh mục
category1 = Category(MaDanhMuc="CAT001", TenDanhMuc="Sofas")
category2 = Category(MaDanhMuc="CAT002", TenDanhMuc="Tables")
db.add_all([category1, category2])
db.commit()

# Thêm sản phẩm
product1 = Product(MaSP="SP001", TenSP="Leather Sofa", Gia=15000000, MaDanhMuc="CAT001")
product2 = Product(MaSP="SP002", TenSP="Wooden Table", Gia=5000000, MaDanhMuc="CAT002")
db.add_all([product1, product2])
db.commit()

db.close()
print("Data seeded successfully!")