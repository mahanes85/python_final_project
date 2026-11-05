from data_access.event_da import EventDa

class EventBl:
    def __init__(self):
        self.event_da = EventDa()

    def save(self, event):
        if not isinstance(event.event_id, int) or event.event_id <= 0:
            raise ValueError("Invalid event ID")

        self.check_event_id(event.event_id)

        if event.event_type in ["Cinema", "Theater", "Concert"]:
            self.event_da.save(event)
        else:
            raise ValueError("Invalid event type")

    def edit(self, event):
        if not isinstance(event.event_id, int) or event.event_id <= 0:
            raise ValueError("Invalid event ID")

        if event.event_type not in ["Cinema", "Theater", "Concert"]:
            raise ValueError("Invalid event type")

        for item in self.event_da.find_all():
            if item.event_id == event.event_id:
                self.event_da.edit(event)
                return

        raise ValueError("Event not found")

    def find_all(self):
        return self.event_da.find_all()

    def check_event_id(self, event_id):
        for event in self.event_da.find_all():
            if event.event_id == event_id:
                raise ValueError("Event ID already exists")