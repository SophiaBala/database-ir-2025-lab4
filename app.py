import yaml
from flask import Flask
from my_project import db
from my_project.auth.domain import Shop, Products, ShopProducts

from my_project.auth.route.shop_route import shop_bp
from my_project.auth.route.products_route import products_bp
from my_project.auth.route.shop_products_route import shop_products_bp
from my_project.auth.route.categories_route import categories_bp

app = Flask(__name__)

with open("config/app.yml", "r") as f:
    config_data = yaml.safe_load(f)

app.config.update(config_data)
db.init_app(app)

app.register_blueprint(shop_bp)
app.register_blueprint(products_bp)
app.register_blueprint(shop_products_bp)
app.register_blueprint(categories_bp)

with app.app_context():
    db.create_all()

print("Database URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))
print("Running on: http://127.0.0.1:5000")


if __name__ == '__main__':
    app.run(debug=True)
