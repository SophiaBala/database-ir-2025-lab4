from my_project import db


class Products(db.Model):
    __tablename__ = 'products'
    idproducts = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(20), unique=True, nullable=False)
    characteristic = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.idcategories', ondelete='CASCADE'))

    shop_products = db.relationship("ShopProducts", backref="product", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "idproducts": self.idproducts,
            "name": self.name,
            "description": self.description,
            "characteristic": self.characteristic,
            "price": self.price,
        }