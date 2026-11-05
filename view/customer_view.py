from tkinter import *
from tkinter import ttk, messagebox

from controller.customer_controller import CustomerController

x_length = 30
y_length = 30
x_distance = 80
y_distance = 40

class CustomerView:
    def __init__(self):
        self.controller = CustomerController()
        self.selected_customer_id = None

        self.win = Toplevel()
        self.win.geometry("650x300")
        self.win.title("Customers")

        Label(self.win, text="Customer Id").place(x=x_length, y=y_length)
        self.customer_id = IntVar()
        Entry(self.win, textvariable=self.customer_id).place(x=x_length + x_distance, y=y_length)

        Label(self.win, text="Name").place(x=x_length, y=y_length + y_distance)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).place(x=x_length + x_distance, y=y_length + y_distance)

        Label(self.win, text="Family").place(x=x_length, y=y_length + 2*y_distance)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family).place(x=x_length + x_distance, y=y_length + 2*y_distance)

        Label(self.win, text="Age").place(x=x_length, y=y_length + 3*y_distance)
        self.age = IntVar()
        Entry(self.win, textvariable=self.age).place(x=x_length + x_distance, y=y_length + 3*y_distance)

        self.table = ttk.Treeview(self.win, show="headings", columns=[1,2,3,4])
        self.table.place(x=x_length + 3*x_distance, y=y_length)

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)

        self.table.heading(1, text="Customer Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Age")

        self.table.bind("<<TreeviewSelect>>", self.table_click)

        Button(self.win, text="Save", command=self.save_click,
               width=10, height=2).place(x=x_length + x_distance, y=y_length + 4*y_distance)

        self.reset_form()

    def reset_form(self):
        self.selected_customer_id = None
        self.customer_id.set(0)
        self.name.set("")
        self.family.set("")
        self.age.set(0)

        for item in self.table.get_children():
            self.table.delete(item)

        for customer in self.controller.find_all()[1]:
            self.table.insert("", END, values=customer.to_tuple())

    def save_click(self):
        if self.selected_customer_id is None:
            success, message = self.controller.save(
                self.customer_id.get(),
                self.name.get(),
                self.family.get(),
                self.age.get()
            )
        else:
            success, message = self.controller.edit(
                self.customer_id.get(),
                self.name.get(),
                self.family.get(),
                self.age.get()
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

        selected_customer = self.table.item(selected[0])["values"]

        if selected_customer:
            self.selected_customer_id = int(selected_customer[0])
            self.customer_id.set(int(selected_customer[0]))
            self.name.set(selected_customer[1])
            self.family.set(selected_customer[2])
            self.age.set(int(selected_customer[3]))