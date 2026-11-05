import os
import pickle

class TicketDa:
    def __init__(self):
        self.filename = "data_access/data/ticket.dat"
        self.ticket_list = self.find_all()

    def save(self, ticket):
        self.ticket_list.append(ticket)
        file = open(self.filename, "wb")
        pickle.dump(self.ticket_list, file)
        file.close()

    def edit(self, ticket):
        found = False

        for index, item in enumerate(self.ticket_list):
            if item.ticket_id == ticket.ticket_id:
                self.ticket_list[index] = ticket
                found = True
                break

        if not found:
            raise ValueError("Ticket not found")

        file = open(self.filename, "wb")
        pickle.dump(self.ticket_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            ticket_list = pickle.load(file)
            file.close()
            return ticket_list