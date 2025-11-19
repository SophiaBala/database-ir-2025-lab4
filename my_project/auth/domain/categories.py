from my_project import db


class Categories(db.Model):
    __tablename__ = 'categories'
    idcategories = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    products = db.relationship("Products", backref="product", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "idcategories": self.idcategories,
            "name": self.name,
        }