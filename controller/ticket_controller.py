from bussines_logic.ticket_bl import TicketBl
from model.ticket import Ticket

class TicketController:
    def __init__(self):
        self.ticket_bl = TicketBl()

    def save(self, ticket_id, customer_id, event_id, status):
        try:
            ticket = Ticket(ticket_id, customer_id, event_id, status)
            self.ticket_bl.save(ticket)
            return True, "Ticket Saved"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def edit(self, ticket_id, customer_id, event_id, status):
        try:
            ticket = Ticket(ticket_id, customer_id, event_id, status)
            self.ticket_bl.edit(ticket)
            return True, "Ticket Updated"
        except Exception as e:
            return False, f"Edit Failed : {e}"

    def find_all(self):
        try:
            ticket_list = self.ticket_bl.find_all()
            return True, ticket_list
        except Exception as e:
            return False, f"Find Failed : {e}"