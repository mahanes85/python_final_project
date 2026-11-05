from bussines_logic.ticket_bl import TicketBl
from controller.ticket_controller import TicketController
from data_access.ticket_da import TicketDa
from model.ticket import Ticket

ticket1 = Ticket(1, 1, 1, "Reserved")
ticket2 = Ticket(2, 2, 1, "Reserved")

#print(ticket1)
#print(ticket2)

# test passed
#ticket_da = TicketDa()
#print(ticket_da.find_all())
#ticket_da.save(ticket1)
#ticket_da.save(ticket2)

# test passed
#bl = TicketBl()
#bl.save(ticket1)
#bl.save(ticket2)
#print(bl.find_all())

# test passed
#controller = TicketController()
#success, message = controller.save(1, 1, 1, "Reserved")
#success, message = controller.save(2, 2, 1, "Reserved")
#print(success)
#print(message)
#print(controller.find_all())

# test passed
#success, message = controller.save(3, 100, 1, "Reserved")
#print(success)
#print(message)