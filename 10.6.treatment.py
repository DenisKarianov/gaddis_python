# program to create an object from classes Patient and Procedure


def main():
    # make class Patient with some data
    class Patient:
        def __init__(self, name, address, phone, contact):
            self.__name = name
            self.__address = address
            self.__phone = phone
            self.__contact = contact

        def set_name(self, name):
            self.__name = name

        def set_address(self, address):
            self.__address = address

        def set_phone(self, phone):
            self.__phone = phone

        def set_contact(self, contact):
            self.__contact = contact

        def get_name(self):
            return self.__name

        def get_address(self):
            return self.__address

        def get_phone(self):
            return self.__phone

        def get_contact(self):
            return self.__contact

        def __str__(self):
            return f"Name: {self.__name}\n" + \
                   f"Address: {self.__address}\n" + \
                   f"Phone: {self.__phone}\n" + \
                   f"Contact person: {self.__contact}"

    # make class Procedure with some data
    class Procedure:
        def __init__(self, name, date, doctor, price):
            self.__name = name
            self.__date = date
            self.__doctor = doctor
            self.__price = price

        def set_name(self, name):
            self.__name = name

        def set_date(self, date):
            self.__date = date

        def set_doctor(self, doctor):
            self.__doctor = doctor

        def set_price(self, price):
            self.__price = price

        def get_name(self):
            return self.__name

        def get_date(self):
            return self.__date

        def get_doctor(self):
            return self.__doctor

        def get_price(self):
            return self.__price

        def __str__(self):
            return f"Procedure: {self.__name}\n" + \
                   f"Date: {self.__date}\n" + \
                   f"Doctor: {self.__doctor}\n" + \
                   f"Price: {self.__price}"

    # create 1 object from class Patient with demo data
    patient1 = Patient('Sarah Connor', "2530 S Malcolm X Blvd, Dallas, TX 75215, USA", "+18007721213", "John Connor "
                                                                                                       "+18007721645")
    # create 3 objects from class Procedure
    proc1 = Procedure("medical examination", "today", "Irwin", 250.00)
    proc2 = Procedure("radiography", "today", "Jamison", 500.00)
    proc3 = Procedure("blood analysis", "today", "Smith", 200.00)
    # print objects' data
    print(patient1)
    print()
    print(proc1)
    print()
    print(proc2)
    print()
    print(proc3)
    print()
    total = proc1.get_price() + proc2.get_price() + proc3.get_price()
    print(f"Total price: ${total}")


# Call the main function.
if __name__ == '__main__':
    main()
