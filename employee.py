# make class Employee with some data
class Employee:
    def __init__(self, name, number, depart, position):
        self.__name = name
        self.__number = number
        self.__depart = depart
        self.__position = position

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_depart(self, depart):
        self.__depart = depart

    def set_position(self, position):
        self.__position = position

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_depart(self):
        return self.__depart

    def get_position(self):
        return self.__position

    def __str__(self):
        return f"Name: {self.__name}\n" + \
            f"Number: {self.__number}\n" + \
            f"Department: {self.__depart}\n" + \
            f"Position: {self.__position}"