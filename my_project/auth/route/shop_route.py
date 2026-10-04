from flask import Blueprint, request, jsonify
from my_project.auth.service.shop_service import ShopService

shop_bp = Blueprint('shop_bp', __name__)

@shop_bp.route('/shop', methods=['GET'])
def get_shop():
    shops = ShopService.get_all_shops()
    return jsonify([
        {"id": s.idshop, "address": s.address, "phone": s.phone, "city": s.city} for s in shops
    ])
    

@shop_bp.route('/shop', methods=['POST'])
def create_shop():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    try:
        new_shop = ShopService.create_shop(data)
        return jsonify(new_shop.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@shop_bp.route('/shop/<int:shop_id>', methods=['PUT'])
def update_shop(shop_id):
    data = request.get_json()
    shop = ShopService.update_shop(shop_id, data)
    if shop:
        return jsonify({
            "id": shop.idshop,
            "address": shop.address,
            "phone": shop.phone,
            "city": shop.city
        })
    return jsonify({"error": "Shop not found"}), 404



@shop_bp.route('/shop/<int:shop_id>', methods=['DELETE'])
def delete_shop(shop_id):
    shop = ShopService.delete_shop(shop_id)
    if shop:
        return jsonify({"message": "Shop deleted"})
    return jsonify({"error": "Shop not found"}), 404