from data_access.payment_da import PaymentDa
from data_access.customer_da import CustomerDa
from data_access.ticket_da import TicketDa

class PaymentBl:
    def __init__(self):
        self.payment_da = PaymentDa()
        self.customer_da = CustomerDa()
        self.ticket_da = TicketDa()

    def save(self, payment):
        self.check_payment_id(payment.payment_id)
        self.customer_exists(payment.customer_id)
        self.ticket_exists(payment.customer_id)

        self.payment_da.save(payment)

    def edit(self, payment):
        self.customer_exists(payment.customer_id)
        self.ticket_exists(payment.customer_id)

        self.payment_da.edit(payment)

    def find_all(self):
        return self.payment_da.find_all()

    def customer_exists(self, customer_id):
        for customer in self.customer_da.find_all():
            if customer.customer_id == customer_id:
                return

        raise ValueError("Customer not found")

    def ticket_exists(self, customer_id):
        for ticket in self.ticket_da.find_all():
            if ticket.customer_id == customer_id and ticket.status == "Reserved":
                return

        raise ValueError("Reserved ticket not found")

    def check_payment_id(self, payment_id):
        for payment in self.payment_da.find_all():
            if payment.payment_id == payment_id:
                raise ValueError("Payment ID already exists")