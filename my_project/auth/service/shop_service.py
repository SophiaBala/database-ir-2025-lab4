from my_project.auth.dao.shop_dao import ShopDAO

class ShopService:

    @staticmethod
    def get_all_shops():
        return ShopDAO.get_all()


    @staticmethod
    def create_shop(data):
        return ShopDAO.create(data)

    @staticmethod
    def update_shop(shop_id, data):
        return ShopDAO.update(shop_id, data)

    @staticmethod
    def delete_shop(shop_id):
        return ShopDAO.delete(shop_id)
