from my_project import db


class Staff(db.Model):
    __tablename__ = 'staff'
    idstaff = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    shop_idshop = db.Column(db.Integer)
    position = db.Column(db.String(50))


    def to_dict(self):
        return {
            "idstaff": self.idstaff,
            "name": self.name,
            "shop_idshop": self.shop_idshop,
            "position": self.position,
        }
    

