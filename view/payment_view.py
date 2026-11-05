from tkinter import *
from tkinter import ttk, messagebox

from controller.payment_controller import PaymentController

x_length = 30
y_length = 30
x_distance = 100
y_distance = 40

class PaymentView:
    def __init__(self):
        self.controller = PaymentController()
        self.selected_payment_id = None

        self.win = Toplevel()
        self.win.geometry("750x350")
        self.win.title("Payments")

        Label(self.win, text="Payment Id").place(x=x_length, y=y_length)
        self.payment_id = IntVar()
        Entry(self.win, textvariable=self.payment_id).place(x=x_length + x_distance, y=y_length)

        Label(self.win, text="Customer Id").place(x=x_length, y=y_length + y_distance)
        self.customer_id = IntVar()
        Entry(self.win, textvariable=self.customer_id).place(x=x_length + x_distance, y=y_length + y_distance)

        Label(self.win, text="Amount").place(x=x_length, y=y_length + 2*y_distance)
        self.amount = DoubleVar()
        Entry(self.win, textvariable=self.amount).place(x=x_length + x_distance, y=y_length + 2*y_distance)

        Label(self.win, text="Status").place(x=x_length, y=y_length + 3*y_distance)
        self.status = StringVar(value="Unpaid")
        ttk.Combobox(self.win,textvariable=self.status,values=["Paid", "Unpaid"],state="readonly"
        ).place(x=x_length + x_distance, y=y_length + 3*y_distance)

        self.table = ttk.Treeview(self.win,show="headings",columns=[1, 2, 3, 4])
        self.table.place(x=350, y=y_length)

        self.table.column(1, width=90)
        self.table.column(2, width=90)
        self.table.column(3, width=100)
        self.table.column(4, width=90)

        self.table.heading(1, text="Payment Id")
        self.table.heading(2, text="Customer Id")
        self.table.heading(3, text="Amount")
        self.table.heading(4, text="Status")

        self.table.bind("<<TreeviewSelect>>", self.table_click)

        Button(self.win,text="Save",command=self.save_click,width=10,height=2
        ).place(x=x_length + x_distance,y=y_length + 4*y_distance)

        self.reset_form()

    def reset_form(self):
        self.selected_payment_id = None
        self.payment_id.set(0)
        self.customer_id.set(0)
        self.amount.set(0)
        self.status.set("Unpaid")

        for item in self.table.get_children():
            self.table.delete(item)

        success, payment_list = self.controller.find_all()

        if success:
            for payment in payment_list:
                self.table.insert("",END,values=payment.to_tuple())

    def save_click(self):
        if self.selected_payment_id is None:
            success, message = self.controller.save(
                self.payment_id.get(),
                self.customer_id.get(),
                self.amount.get(),
                self.status.get()
            )
        else:
            success, message = self.controller.edit(
                self.payment_id.get(),
                self.customer_id.get(),
                self.amount.get(),
                self.status.get()
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

        selected_payment = self.table.item(selected[0])["values"]

        if selected_payment:
            self.selected_payment_id = int(selected_payment[0])
            self.payment_id.set(int(selected_payment[0]))
            self.customer_id.set(int(selected_payment[1]))
            self.amount.set(float(selected_payment[2]))
            self.status.set(selected_payment[3])