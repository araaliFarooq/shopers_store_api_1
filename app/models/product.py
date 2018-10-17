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
        search_keys = ("product", "quantity", "unit_price")
        if all(key in data.keys() for key in search_keys):
            valid = validation.product_validation(data.get("product"), data.get("quantity"), data.get("unit_price"))
            if valid:
                return jsonify({"message":valid}), 400
            product = dict(
                product_id = len(all_products) + 1,
                product = data.get("product"),
                quantity = data.get("quantity"),
                unit_price = data.get("unit_price")
            )
            if any(d["product"] == data.get("product") for d in all_products):
                return jsonify({"message":"product already exists, just update its quantity"}), 409
            all_products.append(product)
            return jsonify({"message":"product successfully added", "products":all_products}), 201
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400

    @staticmethod
    def fetch_all_products():
        # fetch all available products
        if len(all_products) > 0:
            return jsonify({"All Products":all_products}), 200
        return jsonify({"message":"no products added yet"}), 404

    def fetch_single_product(self):
        product_id = self.user_input
        if len(all_products) > 0:
            for product in range(len(all_products)):
                if ((all_products[product]["product_id"]) == int(product_id)):
                    return jsonify({"Product":all_products[product]}),200  
        return jsonify({"message":"no products added yet"}), 404   
        
        

    