from flask import Blueprint, request, jsonify
from my_project.auth.service.shop_products_service import ShopProductsService
from my_project.auth.domain.shop_products import ShopProducts
from my_project.auth.domain.shop import Shop
from my_project.auth.domain.products import Products
from my_project import db


shop_products_bp = Blueprint('shop_products_bp', __name__)

@shop_products_bp.route("/products-shop", methods=["GET"])
def get_products_shop():
    sp_list = ShopProductsService.get_all_products_with_shop()
    result = []
    for sp in sp_list:
        result.append({
            "product_name": sp.product.name,
            "shop_name": sp.shop.address,
            "quantity": sp.quantity,
            "expire_date": sp.expire_date.isoformat()
        })
    return jsonify(result)


@shop_products_bp.route("/by-shop", methods=["GET"])
def get_products_by_shop():
    sp_list = ShopProductsService.get_products_by_shop()
    result = {}
    for sp in sp_list:
        shop_address = sp.shop.address
        if shop_address not in result:
            result[shop_address] = []
        result[shop_address].append({
            "product_name": sp.product.name,
            "description": sp.product.description,
            "characteristic": sp.product.characteristic,
            "price": sp.product.price,
            "expire_date": sp.expire_date.isoformat(),
            "quantity": sp.quantity
        })
    return jsonify(result)

@shop_products_bp.route('/shop_products', methods=['GET'])
def get_shop():
    shop_products = ShopProductsService.get_all_shop_products()
    return jsonify([
        {"id": sp.idstore_product, "expire_date": sp.expire_date, "last_delivery_date": sp.last_delivery_date,
        "quantity": sp.quantity, "shop_idshop": sp.shop_idshop, "products_idproducts": sp.products_idproducts} for sp in shop_products
    ])


@shop_products_bp.route('/shop_products', methods=['POST'])
def create_shop():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    try:
        new_shop_products = ShopProductsService.create_shop(data)
        return jsonify(new_shop_products.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@shop_products_bp.route('/shop_products/<int:shop_products_id>', methods=['PUT'])
def update_shop(shop_products_id):
    data = request.get_json()
    shop_products = ShopProductsService.update_shop(shop_products_id, data)
    if shop_products:
        return jsonify({
            "id": shop_products.idshop,
            "address": shop_products.address,
            "phone": shop_products.phone,
            "city": shop_products.city
        })
    return jsonify({"error": "Shop not found"}), 404



@shop_products_bp.route('/shop/<int:shop_id>', methods=['DELETE'])
def delete_shop(shop_id):
    shop = ShopProductsService.delete_shop(shop_id)
    if shop:
        return jsonify({"message": "Shop deleted"})
    return jsonify({"error": "Shop not found"}), 404


@shop_products_bp.route('/add_shop_product', methods=['POST'])
def add_shop_product():
    data = request.get_json()

    shop_id = data.get("shop_id")
    product_id = data.get("product_id")
    expire_date = data.get("expire_date")
    last_delivery_date = data.get("last_delivery_date")
    quantity = data.get("quantity")

    shop = Shop.query.filter_by(idshop=shop_id).first()
    if not shop:
        return jsonify({"error": "Shop not found"}), 400

    product = Products.query.filter_by(idproducts=product_id).first()
    if not product:
        return jsonify({"error": "Product not found"}), 400

    shop_product = ShopProducts(
        shop_idshop=shop.idshop,
        products_idproducts=product.idproducts,
        expire_date=expire_date,
        last_delivery_date=last_delivery_date,
        quantity=quantity
    )

    db.session.add(shop_product)
    db.session.commit()

    return jsonify({"message": "Inserted successfully"}), 201