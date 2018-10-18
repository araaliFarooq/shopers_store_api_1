"model class for a product"
from app.validation import Validation
from flask import jsonify

all_products=[]
validation = Validation()

class Product:
    def __init__(self, user_input):
        self.user_input = user_input

    def add_product(self):
        #Add product item
        data = self.user_input
        search_keys = ("product_name", "quantity", "unit_price")
        if all(key in data.keys() for key in search_keys):
            
            valid = validation.product_validation(data.get("product_name"), data.get("quantity"), data.get("unit_price"))
            if valid:
                return jsonify({"message":valid}), 400
            product = dict(
                product_id = len(all_products) + 1,
                product_name = data.get("product_name"),
                quantity = data.get("quantity"),
                unit_price = data.get("unit_price")
            )
            if any(d["product_name"] == data.get("product_name") for d in all_products):
                return jsonify({"message":"product already exists, just update its quantity"}), 409       

            all_products.append(product)
            return jsonify({"message":"product successfully added", "products":all_products}), 201
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400     

    