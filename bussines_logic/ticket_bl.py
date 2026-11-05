from data_access.ticket_da import TicketDa
from data_access.event_da import EventDa
from data_access.customer_da import CustomerDa

class TicketBl:
    def __init__(self):
        self.ticket_da = TicketDa()
        self.event_da = EventDa()
        self.customer_da = CustomerDa()

    def save(self, ticket):
        self.check_ticket_id(ticket.ticket_id)
        self.check_event(ticket.event_id)
        self.check_customer(ticket.customer_id)
        self.check_capacity(ticket.event_id)

        self.ticket_da.save(ticket)

    def edit(self, ticket):
        self.check_event(ticket.event_id)
        self.check_customer(ticket.customer_id)

        if ticket.status == "Reserved":
            reserved_count = 0

            for item in self.ticket_da.find_all():
                if (item.event_id == ticket.event_id
                        and item.status == "Reserved"
                        and item.ticket_id != ticket.ticket_id):
                    reserved_count += 1

            event = self.check_event(ticket.event_id)

            if reserved_count >= event.capacity:
                raise ValueError("Event capacity is full")

        self.ticket_da.edit(ticket)

    def find_all(self):
        return self.ticket_da.find_all()

    def check_event(self, event_id):
        for event in self.event_da.find_all():
            if event.event_id == event_id:
                return event
        raise ValueError("Event not found")

    def check_customer(self, customer_id):
        for customer in self.customer_da.find_all():
            if customer.customer_id == customer_id:
                return
        raise ValueError("Customer not found")

    def check_capacity(self, event_id):
        event = self.check_event(event_id)
        reserved_count = 0

        for ticket in self.ticket_da.find_all():
            if ticket.event_id == event_id and ticket.status == "Reserved":
                reserved_count += 1

        if reserved_count >= event.capacity:
            raise ValueError("Event capacity is full")

    def check_ticket_id(self, ticket_id):
        for ticket in self.ticket_da.find_all():
            if ticket.ticket_id == ticket_id:
                raise ValueError("Ticket ID already exists")