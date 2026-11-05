import re

class Validator:
    @staticmethod
    def name_validator(name):
        if not re.match(r"^[a-zA-Z]{1,30}$", name):
            raise ValueError("Invalid name")

    @staticmethod
    def family_validator(family):
        if not re.match(r"^[a-zA-Z]{1,30}$", family):
            raise ValueError("Invalid family")

    @staticmethod
    def age_validator(age):
        if not isinstance(age, int) or not 0 <= age <= 150:
            raise ValueError("Invalid age")

    @staticmethod
    def event_validator(event):
        if not re.match(r"^[a-zA-Z0-9 ]{1,50}$", event):
            raise ValueError("Invalid event")

    @staticmethod
    def capacity_validator(capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Invalid capacity")

    @staticmethod
    def price_validator(price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Invalid price")