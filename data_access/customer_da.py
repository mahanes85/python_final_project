import os
import pickle

class CustomerDa:
    def __init__(self):
        self.filename = "data_access/data/customer.dat"
        self.customer_list = self.find_all()

    def save(self, customer):
        self.customer_list.append(customer)
        file = open(self.filename, "wb")
        pickle.dump(self.customer_list, file)
        file.close()

    def edit(self, customer):
        for index, item in enumerate(self.customer_list):
            if item.customer_id == customer.customer_id:
                self.customer_list[index] = customer
                break
        else:
            raise ValueError("Customer not found")

        file = open(self.filename, "wb")
        pickle.dump(self.customer_list, file)
        file.close()

    def find_all(self):
         if not os.path.exists(self.filename):
            return []
         else:
            file = open(self.filename, "rb")
            customer_list = pickle.load(file)
            file.close()
            return customer_list