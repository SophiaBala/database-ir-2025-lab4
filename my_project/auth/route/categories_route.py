from flask import Blueprint, request, jsonify
from my_project.auth.service.categories_service import CategoriesService
from my_project import db
from sqlalchemy import text

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




@categories_bp.route('/create_random_tables', methods=['POST'])
def trigger_random_tables():
    try:
        db.session.execute(text("CALL create_random_tables()"))
        db.session.commit()
        return jsonify({"message": "Tables created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500