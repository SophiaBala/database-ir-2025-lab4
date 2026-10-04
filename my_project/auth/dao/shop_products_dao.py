from my_project import db
from my_project.auth.domain.shop_products import ShopProducts

class ShopProductsDAO:
    @staticmethod
    def get_all():
        return ShopProducts.query.all()

    @staticmethod
    def get_all_products_with_shop():
        return ShopProducts.query.all()

    @staticmethod
    def get_products_by_shop():
        return ShopProducts.query.all()

    @staticmethod
    def get_by_id(shop_products_id):
        return ShopProducts.query.get(shop_products_id)

    @staticmethod
    def create(data):
        new_shop_products = ShopProducts(
            expire_date=data.get('expire_date'),
            last_delivery_date=data.get('last_delivery_date'),
            quantity=data.get('quantity'),
            shop_idshop=data.get('shop_idshop'),
            products_idproducts=data.get('products_idproducts')
        )
        db.session.add(new_shop_products)
        db.session.commit()
        return new_shop_products

    @staticmethod
    def update(shop_products_id, data):
        shop_products = ShopProducts.query.get(shop_products_id)
        if not shop_products:
            return None

        shop_products.name = data.get('name', shop_products.name)
        shop_products.description = data.get('description', shop_products.description)
        shop_products.characteristic = data.get('characteristic', shop_products.characteristic)
        shop_products.price = data.get('price', shop_products.price)

        db.session.commit()
        return shop_products

    @staticmethod
    def delete(shop_products_id):
        shop_products = ShopProducts.query.get(shop_products_id)
        if not shop_products:
            return None

        db.session.delete(shop_products)
        db.session.commit()
        return shop_products
