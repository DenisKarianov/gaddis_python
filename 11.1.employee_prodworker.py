# make base class Employee and subclass ProductionWorker and program to create object rom class ProductionWorker
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate


def main():
    name = input("Enter employee's name: ")
    # validate number loop
    loop_flag = True
    while loop_flag:
        number = input("Enter employee's number: ")
        if number.isdigit():
            loop_flag = False
            number = int(number)
    # validate shift loop
    loop_flag = 0
    while loop_flag < 2:
        loop_flag = 0  # erase for each iteration
        shift = input("Enter employee's shift (1 - day, 2 - night): ")
        if shift.isdigit():
            loop_flag += 1
            shift = int(shift)
            if shift == 1 or shift == 2:
                loop_flag += 1
    # validate pay rate loop
    loop_flag = True
    while loop_flag:
        pay_rate = input("Enter employee's pay rate: ")
        try:
            pay_rate = float(pay_rate)
            loop_flag = False
        except ValueError:
            print("Pay rate should contain number.")
    # make object from subclass ProductionWorker
    prod_worker = ProductionWorker(name, number, shift, pay_rate)
    print(f"Employee's name: {prod_worker.get_name()}")
    print(f"Employee's number: {prod_worker.get_number()}")
    if prod_worker.get_shift() == 1:
        print("Employee's shift: day")
    else:
        print("Employee's shift: night")
    print(f"Employee's pay rate: ${prod_worker.get_pay_rate()}")


# Call the main function.
if __name__ == '__main__':
    main()
