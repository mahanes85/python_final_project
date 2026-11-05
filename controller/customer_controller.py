from bussines_logic.customer_bl import CustomerBl
from model.customer import Customer

class CustomerController:
    def __init__(self):
        self.customer_bl = CustomerBl()

    def save(self, customer_id, name, family, age):
        try:
            customer = Customer(customer_id, name, family, age)
            self.customer_bl.save(customer)
            return True, "Customer Saved"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def edit(self, customer_id, name, family, age):
        try:
            customer = Customer(customer_id, name, family, age)
            self.customer_bl.edit(customer)
            return True, "Customer Updated"
        except Exception as e:
            return False, f"Edit Failed : {e}"

    def find_all(self):
        try:
            customer_list = self.customer_bl.find_all()
            return True, customer_list
        except Exception as e:
            return False, f"Save Failed : {e}"