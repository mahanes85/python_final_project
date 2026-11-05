from bussines_logic.event_bl import EventBl
from model.event import Event

class EventController:
    def __init__(self):
        self.event_bl = EventBl()

    def save(self, event_id, name, event_type, capacity, price):
        try:
            event = Event(event_id, name, event_type, capacity, price)
            self.event_bl.save(event)
            return True, "Event Saved"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def edit(self, event_id, name, event_type, capacity, price):
        try:
            event = Event(event_id, name, event_type, price, capacity)
            self.event_bl.edit(event)
            return True, "Event Updated"
        except Exception as e:
            return False, f"Edit Failed : {e}"

    def find_all(self):
        try:
            event_list = self.event_bl.find_all()
            return True, event_list
        except Exception as e:
            return False, f"Find Failed : {e}"