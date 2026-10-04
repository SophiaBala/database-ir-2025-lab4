from my_project.auth.dao.products_dao import ProductsDAO

class ProductsService:

    @staticmethod
    def get_all_products():
        return ProductsDAO.get_all()


    @staticmethod
    def create_products(data):
        return ProductsDAO.create(data)

    @staticmethod
    def update_products(products_id, data):
        return ProductsDAO.update(products_id, data)

    @staticmethod
    def delete_products(products_id):
        return ProductsDAO.delete(products_id)
