from bussines_logic.customer_bl import CustomerBl
from controller.customer_controller import CustomerController
from data_access.customer_da import CustomerDa
from model.customer import Customer

customer1 = Customer(1, "Ali", "Ahmadi", 25)
customer2 = Customer(2, "Ahmad", "Vahidi", 18)
#print(customer1)
#print(customer2)

#test passed
#customer_da = CustomerDa()
#print(customer_da.find_all())
#customer_da.save(customer1)
#customer_da.save(customer2)

# test passed
#bl = CustomerBl()
#bl.save(customer1)
#bl.save(customer2)

# test passed
#controller = CustomerController()
#succes, massage = controller.save(1, "Reza", "Ahmadi", 20)
#succes, massage = controller.save(2, "Ahmad", "Vahidi", 180)
#print(succes)
#print(massage)

#Test passed
#bl = CustomerBl()
#bl.save(Customer(1, "Ali", "Ahmadi", 25))