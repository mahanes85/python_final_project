from tools.validation import Validator

class Payment:
    def __init__(self, payment_id, customer_id, amount, status):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.amount = amount
        self.status = status

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        if not isinstance(payment_id, int) or payment_id <= 0:
            raise ValueError("Invalid payment id")
        self.__payment_id = payment_id

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValueError("Invalid customer id")
        self.__customer_id = customer_id

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        Validator.price_validator(amount)
        self.__amount = amount

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status not in ["Paid", "Unpaid"]:
            raise ValueError("Invalid status")
        self.__status = status

    def __repr__(self):
        return f"Payment ({self.payment_id}, {self.customer_id}, {self.amount}, {self.status})"

    def to_tuple(self):
        return self.payment_id, self.customer_id, self.amount, self.status