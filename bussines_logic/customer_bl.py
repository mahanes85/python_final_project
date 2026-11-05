from data_access.customer_da import CustomerDa

class CustomerBl:
    def __init__(self):
        self.customer_da = CustomerDa()

    def save(self, customer):
        if not isinstance(customer.customer_id, int) or customer.customer_id <= 0:
            raise ValueError("Invalid customer ID")

        self.check_customer_id(customer.customer_id)

        if customer.age >= 18:
            self.customer_da.save(customer)
        else:
            raise ValueError("Age must be 18 or older")

    def edit(self, customer):
        if not isinstance(customer.customer_id, int) or customer.customer_id <= 0:
            raise ValueError("Invalid customer ID")

        if customer.age >= 18:
            self.customer_da.edit(customer)
        else:
            raise ValueError("Age must be 18 or older")

    def find_all(self):
        return self.customer_da.find_all()

    def check_customer_id(self, customer_id):
        for customer in self.customer_da.find_all():
            if customer.customer_id == customer_id:
                raise ValueError("Customer ID already exists")