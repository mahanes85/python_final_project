from bussines_logic.payment_bl import PaymentBl
from controller.payment_controller import PaymentController
from data_access.payment_da import PaymentDa
from model.payment import Payment

payment1 = Payment(1, 1, 150000, "Paid")
payment2 = Payment(2, 2, 150000, "Unpaid")

#print(payment1)
#print(payment2)

# test passed
#payment_da = PaymentDa()
#print(payment_da.find_all())
#payment_da.save(payment1)
#payment_da.save(payment2)

# test passed
#bl = PaymentBl()
#bl.save(payment1)
#bl.save(payment2)
#print(bl.find_all())

# test passed
#controller = PaymentController()
#success, message = controller.save(1, 1, 150000, "Paid")
#success, message = controller.save(2, 2, 150000, "Unpaid")
#print(success)
#print(message)
#print(controller.find_all())