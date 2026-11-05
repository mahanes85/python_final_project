from tkinter import *
from tkinter import ttk, messagebox

from controller.event_controller import EventController

x_length = 30
y_length = 30
x_distance = 80
y_distance = 40

class EventView:
    def __init__(self):
        self.controller = EventController()
        self.selected_event_id = None

        self.win = Toplevel()
        self.win.geometry("750x350")
        self.win.title("Events")

        Label(self.win, text="Event Id").place(x=x_length, y=y_length)
        self.event_id = IntVar()
        Entry(self.win, textvariable=self.event_id).place(x=x_length + x_distance, y=y_length)

        Label(self.win, text="Name").place(x=x_length, y=y_length + y_distance)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).place(x=x_length + x_distance, y=y_length + y_distance)

        Label(self.win, text="Event Type").place(x=x_length, y=y_length + 2 * y_distance)
        self.event_type = StringVar()
        ttk.Combobox(self.win,textvariable=self.event_type,
            values=["Cinema", "Theater", "Concert"],state="readonly"
        ).place(x=x_length + x_distance, y=y_length + 2 * y_distance)

        Label(self.win, text="Capacity").place(x=x_length, y=y_length + 3*y_distance)
        self.capacity = IntVar()
        Entry(self.win, textvariable=self.capacity).place(x=x_length + x_distance, y=y_length + 3*y_distance)

        Label(self.win, text="Price").place(x=x_length, y=y_length + 4*y_distance)
        self.price = IntVar()
        Entry(self.win, textvariable=self.price).place(x=x_length + x_distance, y=y_length + 4*y_distance)

        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5])
        self.table.place(x=x_length + 3*x_distance, y=y_length)

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=90)
        self.table.column(4, width=70)
        self.table.column(5, width=90)

        self.table.heading(1, text="Event Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Event Type")
        self.table.heading(4, text="Capacity")
        self.table.heading(5, text="Price")

        self.table.bind("<<TreeviewSelect>>", self.table_click)

        Button(self.win, text="Save", command=self.save_click,
               width=10, height=2).place(x=x_length + x_distance, y=y_length + 5*y_distance)

        self.reset_form()

    def reset_form(self):
        self.selected_event_id = None
        self.event_id.set(0)
        self.name.set("")
        self.event_type.set("")
        self.capacity.set(0)
        self.price.set(0)

        for item in self.table.get_children():
            self.table.delete(item)

        for event in self.controller.find_all()[1]:
            self.table.insert("", END, values=event.to_tuple())

    def save_click(self):
        if self.selected_event_id is None:
            success, message = self.controller.save(
                self.event_id.get(),
                self.name.get(),
                self.event_type.get(),
                self.capacity.get(),
                self.price.get()
            )
        else:
            success, message = self.controller.edit(
                self.event_id.get(),
                self.name.get(),
                self.event_type.get(),
                self.capacity.get(),
                self.price.get()
            )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected = self.table.selection()

        if not selected:
            return

        selected_event = self.table.item(selected[0])["values"]

        if selected_event:
            self.selected_event_id = int(selected_event[0])
            self.event_id.set(int(selected_event[0]))
            self.name.set(selected_event[1])
            self.event_type.set(selected_event[2])
            self.capacity.set(int(selected_event[3]))
            self.price.set(int(selected_event[4]))