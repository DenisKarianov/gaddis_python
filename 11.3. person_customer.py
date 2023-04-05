# make base class Person and subclass Customer and program to create object from the subclass
# global constants
NAME = 'Penelopa'
ADDRESS = 'Santa-Cruz'
PHONE = '+34149874694'
NUMBER = '242'
MAIL_LIST = True


class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


class Customer(Person):
    def __init__(self, name, address, phone, number, mail_list):
        Person.__init__(self, name, address, phone)
        self.__number = number
        self.__mail_list = mail_list

    def get_number(self):
        return self.__number

    def get_mail_list(self):
        return self.__mail_list


def main():
    # make object from class Customer
    demo_customer = Customer(NAME, ADDRESS, PHONE, NUMBER, MAIL_LIST)
    print("Customer's data")
    print("---------------------------")
    print(demo_customer.get_name())
    print(demo_customer.get_address())
    print(demo_customer.get_phone())
    print(demo_customer.get_number())
    print(demo_customer.get_mail_list())


# Call the main function.
if __name__ == '__main__':
    main()
