from my_project import db


class Shop(db.Model):
    __tablename__ = 'shop'
    idshop = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50))
    phone = db.Column(db.String(20), unique=True, nullable=False)
    city = db.Column(db.String(100), nullable=False)

    orders = db.relationship("Order", backref="shop", cascade="all, delete-orphan")
    shop_products = db.relationship("ShopProducts", backref="shop", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "idshop": self.idshop,
            "address": self.address,
            "phone": self.phone,
            "city": self.city,
        }

class Order(db.Model):
    __tablename__ = 'orders'
    idorders = db.Column(db.Integer, primary_key=True)
    shop_idshop = db.Column(db.Integer, db.ForeignKey('shop.idshop', ondelete='CASCADE'))
    items = db.relationship("OrderItem", backref="order", cascade="all, delete-orphan")

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    idorder_items = db.Column(db.Integer, primary_key=True)
    orders_idorders = db.Column(db.Integer, db.ForeignKey('orders.idorders', ondelete='CASCADE'))
