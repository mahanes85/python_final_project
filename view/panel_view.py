from tkinter import *
from view import *

x_length = 30
y_length = 30
y_distance = 60

class PanelView:
    def customers_click(self):
        customer_ui = CustomerView()

    def events_click(self):
        event_ui = EventView()

    def tickets_click(self):
        ticket_ui = TicketView()

    def payments_click(self):
        payment_ui = PaymentView()

    def __init__(self):
        self.win = Tk()
        self.win.geometry("300x300")
        self.win.title("Main Panel")

        Button(self.win, text="Customers", command=self.customers_click, width=10, height=2).place(x=x_length,y=y_length)
        Button(self.win, text="Events", command=self.events_click, width=10, height=2).place(x=x_length, y=y_length + y_distance)
        Button(self.win, text="Tickets", command=self.tickets_click, width=10, height=2).place(x=x_length, y=y_length + 2*y_distance)
        Button(self.win, text="Payments", command=self.payments_click, width=10, height=2).place(x=x_length, y=y_length + 3*y_distance)

        self.win.mainloop()