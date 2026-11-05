import os
import pickle

class PaymentDa:
    def __init__(self):
        self.filename = "data_access/data/payment.dat"
        self.payment_list = self.find_all()

    def save(self, payment):
        self.payment_list.append(payment)
        file = open(self.filename, "wb")
        pickle.dump(self.payment_list, file)
        file.close()

    def edit(self, payment):
        for index, item in enumerate(self.payment_list):
            if item.payment_id == payment.payment_id:
                self.payment_list[index] = payment
                break
        else:
            raise ValueError("Payment not found")

        file = open(self.filename, "wb")
        pickle.dump(self.payment_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            payment_list = pickle.load(file)
            file.close()
            return payment_list