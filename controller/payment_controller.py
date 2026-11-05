from bussines_logic.payment_bl import PaymentBl
from model.payment import Payment

class PaymentController:
    def __init__(self):
        self.payment_bl = PaymentBl()

    def save(self, payment_id, customer_id, amount, status):
        try:
            payment = Payment(payment_id, customer_id, amount, status)
            self.payment_bl.save(payment)
            return True, "Payment Saved"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def edit(self, payment_id, customer_id, amount, status):
        try:
            payment = Payment(payment_id, customer_id, amount, status)
            self.payment_bl.edit(payment)
            return True, "Payment Updated"
        except Exception as e:
            return False, f"Edit Failed : {e}"

    def find_all(self):
        try:
            payment_list = self.payment_bl.find_all()
            return True, payment_list
        except Exception as e:
            return False, f"Find Failed : {e}"