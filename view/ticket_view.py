from tkinter import *
from tkinter import ttk, messagebox

from controller.ticket_controller import TicketController
from controller.event_controller import EventController

x_length = 30
y_length = 30
x_distance = 100
y_distance = 40

class TicketView:
    def __init__(self):
        self.controller = TicketController()
        self.event_controller = EventController()
        self.selected_ticket_id = None

        self.win = Toplevel()
        self.win.geometry("750x400")
        self.win.title("Tickets")

        Label(self.win, text="Ticket Id").place(x=x_length, y=y_length)
        self.ticket_id = IntVar()
        Entry(self.win, textvariable=self.ticket_id).place(x=x_length + x_distance, y=y_length)

        Label(self.win, text="Customer Id").place(x=x_length, y=y_length + y_distance)
        self.customer_id = IntVar()
        Entry(self.win, textvariable=self.customer_id).place(x=x_length + x_distance, y=y_length + y_distance)

        Label(self.win, text="Event").place(x=x_length, y=y_length + 2*y_distance)
        self.event_id = StringVar()
        self.event_box = ttk.Combobox(self.win,textvariable=self.event_id,state="readonly")
        self.event_box.place(x=x_length + x_distance, y=y_length + 2*y_distance)
        self.event_box.bind("<<ComboboxSelected>>", self.event_selected)

        Label(self.win, text="Status").place(x=x_length, y=y_length + 3*y_distance)
        self.status = StringVar(value="Reserved")
        ttk.Combobox(self.win,textvariable=self.status,values=["Reserved", "Cancelled"],state="readonly"
        ).place(x=x_length + x_distance, y=y_length + 3*y_distance)

        self.capacity_label = Label(self.win, text="Capacity: -")
        self.capacity_label.place(x=x_length, y=y_length + 4*y_distance)

        self.reserved_label = Label(self.win, text="Reserved: -")
        self.reserved_label.place(x=x_length, y=y_length + 5*y_distance)

        self.remaining_label = Label(self.win, text="Remaining: -")
        self.remaining_label.place(x=x_length, y=y_length + 6*y_distance)

        self.table = ttk.Treeview(self.win,show="headings",columns=[1, 2, 3, 4])
        self.table.place(x=350, y=y_length)

        self.table.column(1, width=70)
        self.table.column(2, width=90)
        self.table.column(3, width=90)
        self.table.column(4, width=100)

        self.table.heading(1, text="Ticket Id")
        self.table.heading(2, text="Customer Id")
        self.table.heading(3, text="Event Id")
        self.table.heading(4, text="Status")

        self.table.bind("<<TreeviewSelect>>", self.table_click)

        Button(self.win,text="Save",command=self.save_click,width=10,height=2
        ).place(x=x_length + x_distance, y=y_length + 7*y_distance)

        self.reset_form()

    def load_events(self):
        success, event_list = self.event_controller.find_all()

        if success:
            self.events = event_list
            self.event_box["values"] = [f"{event.event_id} - {event.name}"for event in self.events]

    def event_selected(self, event):
        selected = self.event_box.get()

        if not selected:
            self.capacity_label.config(text="Capacity: -")
            self.reserved_label.config(text="Reserved: -")
            self.remaining_label.config(text="Remaining: -")
            return

        event_id = int(selected.split(" - ")[0])

        for item in self.events:
            if item.event_id == event_id:
                reserved_count = sum(
                    1 for ticket in self.controller.find_all()[1]
                    if ticket.event_id == event_id
                    and ticket.status == "Reserved"
                )

                self.capacity_label.config(text=f"Capacity: {item.capacity}")
                self.reserved_label.config(text=f"Reserved: {reserved_count}")
                self.remaining_label.config(text=f"Remaining: {item.capacity - reserved_count}")
                break

    def reset_form(self):
        self.selected_ticket_id = None

        self.ticket_id.set(0)
        self.customer_id.set(0)
        self.event_id.set("")
        self.status.set("Reserved")

        for item in self.table.get_children():
            self.table.delete(item)

        success, ticket_list = self.controller.find_all()

        if success:
            for ticket in ticket_list:
                self.table.insert("", END, values=ticket.to_tuple())

        self.load_events()

    def save_click(self):
        selected = self.event_box.get()

        if not selected:
            messagebox.showerror("Error", "Please select an event")
            return

        event_id = int(selected.split(" - ")[0])

        if self.selected_ticket_id is None:
            success, message = self.controller.save(
                self.ticket_id.get(),
                self.customer_id.get(),
                event_id,
                self.status.get()
            )
        else:
            success, message = self.controller.edit(
                self.ticket_id.get(),
                self.customer_id.get(),
                event_id,
                self.status.get()
            )

        if success:
            messagebox.showinfo("Success", message)

            self.reset_form()

            self.event_box.set(selected)
            self.event_selected(None)

        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected = self.table.selection()

        if not selected:
            return

        selected_ticket = self.table.item(selected[0])["values"]

        if selected_ticket:
            self.selected_ticket_id = int(selected_ticket[0])
            self.ticket_id.set(int(selected_ticket[0]))
            self.customer_id.set(int(selected_ticket[1]))
            self.status.set(selected_ticket[3])

            for item in self.events:
                if item.event_id == int(selected_ticket[2]):
                    self.event_box.set(
                        f"{item.event_id} - {item.name}"
                    )
                    self.event_selected(None)
                    break