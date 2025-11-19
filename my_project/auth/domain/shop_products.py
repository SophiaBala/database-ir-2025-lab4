from my_project import db
from datetime import date

class ShopProducts(db.Model):
    __tablename__ = 'shop_products'
    __table_args__ = (
        db.PrimaryKeyConstraint('shop_idshop', 'products_idproducts', 'idstore_product'),
    )
    idstore_product = db.Column(db.Integer, nullable=False)
    shop_idshop = db.Column(db.Integer, db.ForeignKey('shop.idshop', ondelete='CASCADE'), nullable=False)
    products_idproducts = db.Column(db.Integer, db.ForeignKey('products.idproducts', ondelete='CASCADE'), nullable=False)
    expire_date = db.Column(db.Date, nullable=False)
    last_delivery_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "shop_idshop": self.shop_idshop,
            "products_idproducts": self.products_idproducts,
            "expire_date": self.expire_date.isoformat(),
            "last_delivery_date": self.last_delivery_date.isoformat(),
            "quantity": self.quantity,
        }