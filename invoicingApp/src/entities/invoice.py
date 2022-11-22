import uuid

class Invoice:
    def __init__(self, invoice_id, date, user_id,user_name, user_address, user_phone, customer_name, customer_shipping_address, product_description, amount, unit_price, tax, logo):
        self.id = uuid.uuid1().hex
        self.user = invoice_id
        self.date = date
        self.user_id = user_id
        self.user_name= user_name
        self.user_address = user_address
        self.user_phone= user_phone
        self.customer_name= customer_name
        self.customer_shipping_address=customer_shipping_address
        self.product_description= product_description
        self.amount=amount
        self.unit_price= unit_price
        self.tax= tax
        self.logo= logo
