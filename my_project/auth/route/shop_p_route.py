from flask import Blueprint, request, jsonify
from my_project import db
from my_project.auth.domain import Shop, Product, ShopProduct  # твої моделі

shop_product_bp = Blueprint('shop_product_bp', __name__)


