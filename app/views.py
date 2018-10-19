from app import app
from flask import request, jsonify
from .models.product import Product
from .models.sales import SaleRecord
from app.validation import Validation

product_obj = Product()
sale_obj = SaleRecord()
validation_obj = Validation()

"""Product Views"""
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

"""Sales View"""
@app.route("/api/v1/sales", methods=["POST"])
#adding sales recotd
def create_sales_record():
    data = request.get_json()
    search_keys = ( "product","quantity", "amount")
    if all(key in data.keys() for key in search_keys):
        product = data.get("product")
        quantity = data.get("quantity")
        amount = data.get("amount")

        invalid_values = validation_obj.product_validation(product, quantity, amount)
        if invalid_values:
            return jsonify({"message":invalid_values}), 400
        if (sale_obj.create_sale_record(product, quantity, amount)):
            return jsonify({"message":"Sale record successfully created", "Sales":sale_obj.all_Sales}), 201
        else:
            return jsonify({"message":"sale record not created or no products added yet"}), 400
    else:
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400

@app.route("/api/v1/sales", methods=["GET"])
# fetching all sales
def fetch_all_sales():
    all_sales = sale_obj.fetch_all_sales()
    if all_sales:
        return jsonify({"All Sales":sale_obj.all_Sales}), 200
    return jsonify({"message":"no sales created yet"}), 404 

@app.route("/api/v1/sales/<sale_id>", methods=["GET"])
# fetching a single product
def fetch_single_sale(sale_id):
    invalid = validation_obj.validate_input_type(sale_id)
    if invalid:
        return jsonify({"message":invalid}), 400
    single_sale = sale_obj.fetch_single_sale(sale_id)
    if single_sale:
        return jsonify({"sale details": single_sale}), 200
    return jsonify({"message":"sale not created yet"}), 404

