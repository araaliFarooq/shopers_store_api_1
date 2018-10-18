from app import app
from flask import request
from .models.product import Product

@app.route("/api/v1/products",methods=["POST"])
#adding product
def add_product():
    add_product = Product(request.get_json())
    new_product = add_product.add_product()
    return new_product

