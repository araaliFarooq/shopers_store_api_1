"model class for a product"

class Product(object):
    def __init__(self):
        self.all_products = []

    def add_product(self, product, quantity, unit_price):
        #Add product item
        product = dict(
                product_id = len(self.all_products) + 1,
                product = product,
                quantity = quantity,
                unit_price = unit_price
            )
        self.all_products.append(product)
        return self.all_products

    def fetch_all_products(self):
        # fetch all available products
        if len(self.all_products) > 0:
            return self.all_products
        return False

    def fetch_single_product(self, product_id):
        # fetch a single product
        if len(self.all_products) > 0:
            for product in range(len(self.all_products)):
                if ((self.all_products[product]["product_id"]) == int(product_id)):
                    return self.all_products[product]
                return False    
        return False
      