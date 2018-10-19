from app.models.sales import SaleRecord
from tests.base_test import BaseTestCase
from flask import json

sales_obj = SaleRecord()
class TestSales(BaseTestCase):

    def test_data_structure(self):
        self.assertTrue(isinstance(sales_obj.all_Sales, list))

    def test_creating_sale(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Sale record successfully created")
        self.assertEquals(response.status_code, 201)

    def test_creating_sale_with_no_product(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product=" ", quantity="20", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "product name is missing")
        self.assertEquals(response.status_code, 400)

    def test_creating_sale_with_no_quantity(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="hhhhh", quantity=" ", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "quantity must be only digits and must have no white spaces")
        self.assertEquals(response.status_code, 400)

    def test_creating_sale_with_quantity_spaces(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="hhhhh", quantity=" 20", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "quantity must be only digits and must have no white spaces")
        self.assertEquals(response.status_code, 400)

    def test_creating_sale_with_product_spaces(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product=" hhhhh", quantity="20", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "product name must have no white spaces")
        self.assertEquals(response.status_code, 400)

    def test_creating_sale_with_short_product_name(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="hh", quantity="20", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "product name should be more than 4 characters long")
        self.assertEquals(response.status_code, 400)

    def test_creating_sale_with_wrong_quantity(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="hhsss", quantity="0", amount="200"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "quantity should be at least 1 item")
        self.assertEquals(response.status_code, 400)

    def test_creating_sale_with_wrong_price(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="hhsss", quantity="20", amount="0"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "unit price should be greater than zero")
        self.assertEquals(response.status_code, 400)  

    def test_creating_sale_with_missing_key(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(quantity="20", amount="0"),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "a 'key(s)' is missing in your request body")
        self.assertEquals(response.status_code, 400)                    

    def test_fetching_sales(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)
         
    def test_fetching_single_sale(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales/1",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)

    def test_fetching_not_existing_single_sale(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales/12",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 404)    

    def test_fetching_single_sale_with_impromper_id(self):
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Shirts", quantity="20", unit_price="200"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales/q",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"], "Input should be an interger")
        self.assertEquals(response2.status_code, 400)               