from flask import Blueprint, request, jsonify
from my_project.auth.service.products_service import ProductsService

products_bp = Blueprint('products_bp', __name__)

@products_bp.route('/products', methods=['GET'])
def get_shop():
    products = ProductsService.get_all_products()
    return jsonify([
        {"id": p.idproducts, "name": p.name, "description": p.description, "characteristic": p.price, "price": p.characteristic} for p in products
    ])
    

@products_bp.route('/products', methods=['POST'])
def create_products():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    try:
        new_products = ProductsService.create_products(data)
        return jsonify(new_products.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@products_bp.route('/products/<int:products_id>', methods=['PUT'])
def update_shop(products_id):
    data = request.get_json()
    products = ProductsService.update_products(products_id, data)
    if products:
        return jsonify({
            "idproducts": products.idproducts,
            "name": products.name,
            "description": products.description,
            "characteristic": products.characteristic,
            "price": products.price,
        })
    return jsonify({"error": "Shop not found"}), 404



@products_bp.route('/products/<int:products_id>', methods=['DELETE'])
def delete_products(products_id):
    products = ProductsService.delete_products(products_id)
    if products:
        return jsonify({"message": "Product deleted"})
    return jsonify({"error": "Product not found"}), 404