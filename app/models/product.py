"model class for a product"

class Product:
    def __init__(self):
        self.all_products = []

    def add_product(self, product, quantity, unit_price):
        #Add product item
        product = dict(
                product_id = len(self.all_products) + 1,
                product_name = product,
                quantity = quantity,
                unit_price = unit_price
            )
        self.all_products.append(product)
        return True
        