from tools.validation import Validator

class Event:
    def __init__(self, event_id, name, event_type, capacity, price):
        self.event_id = event_id
        self.name = name
        self.event_type = event_type
        self.capacity = capacity
        self.price = price

    @property
    def event_id(self):
        return self.__event_id

    @event_id.setter
    def event_id(self, event_id):
        if not isinstance(event_id, int) or event_id <= 0:
            raise ValueError("Invalid event id")
        self.__event_id = event_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.name_validator(name)
        self.__name = name

    @property
    def event_type(self):
        return self.__event_type

    @event_type.setter
    def event_type(self, event_type):
        Validator.event_validator(event_type)
        self.__event_type = event_type

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        Validator.capacity_validator(capacity)
        self.__capacity = capacity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        Validator.price_validator(price)
        self.__price = price

    def __repr__(self):
        return f"Event ({self.event_id}, {self.name}, {self.event_type}, {self.capacity}, {self.price})"

    def to_tuple(self):
        return self.event_id, self.name, self.event_type, self.capacity, self.price