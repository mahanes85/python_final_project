import os
import pickle

class EventDa:
    def __init__(self):
        self.filename = "data_access/data/event.dat"
        self.event_list = self.find_all()

    def save(self, event):
        self.event_list.append(event)
        file = open(self.filename, "wb")
        pickle.dump(self.event_list, file)
        file.close()

    def edit(self, event):
        for index, item in enumerate(self.event_list):
            if item.event_id == event.event_id:
                self.event_list[index] = event
                break
        else:
            raise ValueError("Event not found")

        file = open(self.filename, "wb")
        pickle.dump(self.event_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            event_list = pickle.load(file)
            file.close()
            return event_list