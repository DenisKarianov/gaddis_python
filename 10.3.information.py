# program to create an object from class Information


def main():
    # make class Information with personal data
    class Information:
        def __init__(self, name, address, age, phone):
            self.__name = name
            self.__address = address
            self.__age = age
            self.__phone = phone

        def set_name(self, name):
            self.__name = name

        def set_address(self, address):
            self.__address = address

        def set_age(self, age):
            self.__age = age

        def set_phone(self, phone):
            self.__phone = phone

        def get_name(self):
            return self.__name

        def get_address(self):
            return self.__address

        def get_age(self):
            return self.__age

        def get_phone(self):
            return self.__phone

    # create 3 objects from class Information
    info1 = Information("Atos", "Paris, rue du Ferou, 5", "31", "+33 1 42 96 70 00")
    info2 = Information("Portos", "Paris, rue du Vieux Colombier, 6", "28", "+33 1 42 96 70 04")
    info3 = Information("Aramis", "Paris, rue du Servadoni, 25", "23", "+33 1 42 96 70 17")
    print(info1.get_name())
    print(info1.get_address())
    print()
    print(info2.get_name())
    print(info2.get_address())
    print()
    print(info3.get_name())
    print(info3.get_address())


# Call the main function.
if __name__ == '__main__':
    main()
