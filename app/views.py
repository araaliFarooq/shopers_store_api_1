from app import app
from flask import request, jsonify
from .models.product import Product
from app.validation import Validation

product_obj = Product()
validation_obj = Validation()

@app.route("/api/v1/products",methods=["POST"])
#adding product
def add_product():
    data = request.get_json()
    search_keys = ("product", "quantity", "unit_price")
    if all(key in data.keys() for key in search_keys):
        product = data.get("product")
        quantity = data.get("quantity")
        unit_price = data.get("unit_price")

        invalid = validation_obj.product_validation(product, quantity, unit_price)
        if invalid:
            return jsonify({"message":invalid}), 400
        if any(prodct["product"] == product for prodct in product_obj.all_products):
            return jsonify({"message":"product already exists, just update its quantity"}), 409
        if (product_obj.add_product(product, quantity, unit_price)):
            return jsonify({"message":"product successfully added", "products":product_obj.all_products}), 201
    return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400 

@app.route("/api/v1/products", methods=["GET"])
# fetching all products
def fetch_all_products():
    all_products = product_obj.fetch_all_products()
    if all_products:
        return jsonify({"All Products":all_products}), 200
    return jsonify({"message":"no products added yet"}), 404 

@app.route("/api/v1/products/<product_id>", methods=["GET"])
# fetching a single product
def fetch_single_product(product_id):
    invalid = validation_obj.validate_input_type(product_id)
    if invalid:
        return jsonify({"message":invalid}), 400
    single_product = product_obj.fetch_single_product(product_id)
    if single_product:
        return jsonify({"product details": single_product}), 200
    return jsonify({"message":"product not added yet"}), 404    

