from tools.validation import Validator

class Ticket:
    def __init__(self, ticket_id, customer_id, event_id, status):
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.event_id = event_id
        self.status = status

    @property
    def ticket_id(self):
        return self.__ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        if not isinstance(ticket_id, int) or ticket_id <= 0:
            raise ValueError("Invalid ticket id")
        self.__ticket_id = ticket_id

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValueError("Invalid customer id")
        self.__customer_id = customer_id

    @property
    def event_id(self):
        return self.__event_id

    @event_id.setter
    def event_id(self, event_id):
        if not isinstance(event_id, int) or event_id <= 0:
            raise ValueError("Invalid event id")
        self.__event_id = event_id

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status not in ["Reserved", "Cancelled"]:
            raise ValueError("Invalid status")
        self.__status = status

    def __repr__(self):
        return f"Ticket ({self.ticket_id}, {self.customer_id}, {self.event_id}, {self.status})"

    def to_tuple(self):
        return self.ticket_id, self.customer_id, self.event_id, self.status