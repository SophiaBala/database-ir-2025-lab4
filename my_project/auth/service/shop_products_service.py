from my_project.auth.dao.shop_products_dao import ShopProductsDAO

class ShopProductsService:

    @staticmethod
    def get_products_by_shop():
        return ShopProductsDAO.get_products_by_shop()

    @staticmethod
    def get_all_products_with_shop():
        return ShopProductsDAO.get_all_products_with_shop()

    @staticmethod
    def get_all_shop_products():
        return ShopProductsDAO.get_all()


    @staticmethod
    def create_shop_products(data):
        return ShopProductsDAO.create(data)

    @staticmethod
    def update_shop_products(shop_products_id, data):
        return ShopProductsDAO.update(shop_products_id, data)

    @staticmethod
    def delete_shop_products(shop_products_id):
        return ShopProductsDAO.delete(shop_products_id)
