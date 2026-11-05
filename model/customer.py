from tools.validation import Validator

class Customer:
    def __init__(self, customer_id, name, family, age):
        self.customer_id = customer_id
        self.name = name
        self.family = family
        self.age = age

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValueError("Invalid customer id")
        self.__customer_id = customer_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.name_validator(name)
        self.__name = name

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        Validator.family_validator(family)
        self.__family = family

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        Validator.age_validator(age)
        self.__age = age

    def __repr__(self):
        return f"Customer ({self.customer_id}, {self.name}, {self.family}, {self.age})"

    def to_tuple(self):
        return self.customer_id, self.name, self.family, self.age