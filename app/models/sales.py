"model class for a sales_record"
from app.models.product import Product
from datetime import datetime

product_obj = Product()

class SaleRecord:
    def __init__(self):
        self.all_Sales = []

    def create_sale_record(self, product, quantity, amount):
        # create a sales record
        sale_record = dict(
            sale_id = len(self.all_Sales)+1,
            product = product,
            quantity = quantity,
            amount = amount,
            attendant = "attendants_name",
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.all_Sales.append(sale_record)
        return True

    # def create_sale_record(self, product_id, quantity):
    #     # create a sales record from existing productsif len(self.all_products) > 0:
    #     if len(product_obj.all_products) > 0:
    #         for product in range(len(product_obj.all_products)):
    #             if ((product_obj.all_products[product]["product_id"]) == int(product_id)):
    #                 sale_record = dict(
    #                     sale_id = len(self.all_Sales)+1,
    #                     product = product_obj.all_products[product]["product"],
    #                     quantity = quantity,
    #                     amount = (int(product_obj.all_products[product]["unit_price"]))*int(quantity),
    #                     attendant = "attendants_name",
    #                     date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #                 )
    #                 self.all_Sales.append(sale_record)
    #                 return True
    #     else:
    #         return False

    def fetch_all_sales(self):
        # fetch all available sales
        if len(self.all_Sales) > 0:
            return self.all_Sales
        return False

    def fetch_single_sale(self, sale_id):
        # fetch a single sale
        if len(self.all_Sales) > 0:
            for sale in range(len(self.all_Sales)):
                if ((self.all_Sales[sale]["sale_id"]) == int(sale_id)):
                    return self.all_Sales[sale]
                return False    
        return False    

