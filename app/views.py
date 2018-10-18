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
    


