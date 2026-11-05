from bussines_logic.event_bl import EventBl
from controller.event_controller import EventController
from data_access.event_da import EventDa
from model.event import Event

event1 = Event(1, "Cinema1", "Cinema", 100, 150000)
event2 = Event(2, "Cinema2", "Cinema", 80, 120000)
event3 = Event(3, "Theater", "Theater", 50, 200000)
event4 = Event(4, "Concert", "Concert", 200, 300000)

#print(event1)
#print(event2)
#print(event3)
#print(event4)

# test passed
#event_da = EventDa()
#print(event_da.find_all())
#event_da.save(event1)
#event_da.save(event2)
#event_da.save(event3)
#event_da.save(event4)

# test passed
#bl = EventBl()
#bl.save(event1)
#bl.save(event2)
#bl.save(event3)
#bl.save(event4)
#print(bl.find_all())

# test passed
#controller = EventController()
#success, message = controller.save(1, "Cinema1", "Cinema", 100, 150000)
#success, message = controller.save(2, "Cinema2", "Cinema", 80, 120000)
#success, message = controller.save(3, "Theater", "Theater", 50, 200000)
#success, message = controller.save(4, "Concert", "Concert", 200, 300000)
#print(success)
#print(message)
#print(controller.find_all())