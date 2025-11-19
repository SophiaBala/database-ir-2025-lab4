from my_project import db
from my_project.auth.domain.categories import Categories

class CategoriesDAO:
    @staticmethod
    def get_all_with_products():
        return Categories.query.all()




