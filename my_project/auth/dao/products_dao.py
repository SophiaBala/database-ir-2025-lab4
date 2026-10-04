from my_project import db
from my_project.auth.domain.products import Products

class ProductsDAO:
    @staticmethod
    def get_all():
        return Products.query.all()

    @staticmethod
    def get_by_id(products_id):
        return Products.query.get(products_id)

    @staticmethod
    def create(data):
        new_products = Products(
            name=data.get('name'),
            description=data.get('description'),
            characteristic=data.get('characteristic'),
            price=data.get('price')
        )
        db.session.add(new_products)
        db.session.commit()
        return new_products

    @staticmethod
    def update(products_id, data):
        products = Products.query.get(products_id)
        if not products:
            return None

        products.name = data.get('name', products.name)
        products.description = data.get('description', products.description)
        products.characteristic = data.get('characteristic', products.characteristic)
        products.price = data.get('price', products.price)

        db.session.commit()
        return products

    @staticmethod
    def delete(products_id):
        products = Products.query.get(products_id)
        if not products:
            return None

        db.session.delete(products)
        db.session.commit()
        return products
