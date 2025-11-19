from my_project.auth.dao.categories_dao import CategoriesDAO

class CategoriesService:

    @staticmethod
    def get_all_with_products():
        return CategoriesDAO.get_all_with_products()


