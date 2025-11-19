from flask import Blueprint, request, jsonify
from my_project.auth.service.categories_service import CategoriesService


categories_bp = Blueprint("categories_bp", __name__, url_prefix="/categories")

@categories_bp.route("/with-products", methods=["GET"])
def get_categories_with_products():
    categories = CategoriesService.get_all_with_products()
    result = []
    for cat in categories:
        result.append({
            "category_name": cat.name,
            "products": [p.name for p in cat.products]
        })
    return jsonify(result)