from my_project import db
from my_project.auth.domain.shop import Shop

class ShopDAO:
    @staticmethod
    def get_all():
        return Shop.query.all()

    @staticmethod
    def get_by_id(shop_id):
        return Shop.query.get(shop_id)

    @staticmethod
    def create(data):
        new_shop = Shop(
            address=data.get('address'),
            phone=data.get('phone'),
            city=data.get('city')
        )
        db.session.add(new_shop)
        db.session.commit()
        return new_shop

    @staticmethod
    def update(shop_id, data):
        shop = Shop.query.get(shop_id)
        if not shop:
            return None

        shop.address = data.get('address', shop.address)
        shop.phone = data.get('phone', shop.phone)
        shop.city = data.get('city', shop.city)

        db.session.commit()
        return shop

    @staticmethod
    def delete(shop_id):
        shop = Shop.query.get(shop_id)
        if not shop:
            return None

        db.session.delete(shop)
        db.session.commit()
        return shop
