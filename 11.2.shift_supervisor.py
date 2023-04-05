# make base class Employee and subclass ShiftSupervisor and program to create object from the subclass
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


class ShiftSupervisor(Employee):
    def __init__(self, name, number, ann_salary, ann_bonus):
        Employee.__init__(self, name, number)
        self.__ann_salary = ann_salary
        self.__ann_bonus = ann_bonus

    def set_ann_salary(self, ann_salary):
        self.__ann_salary = ann_salary

    def set_ann_bonus(self, ann_bonus):
        self.__ann_bonus = ann_bonus

    def get_ann_salary(self):
        return self.__ann_salary

    def get_ann_bonus(self):
        return self.__ann_bonus


def main():
    name = input("Enter ShiftSupervisor's name: ")
    # validate number loop
    loop_flag = True
    while loop_flag:
        number = input("Enter ShiftSupervisor's number: ")
        if number.isdigit():
            loop_flag = False
            number = int(number)
    # validate salary loop
    loop_flag = True
    while loop_flag:
        ann_salary = input("Enter ShiftSupervisor's annual salary: ")
        try:
            ann_salary = float(ann_salary)
            loop_flag = False
        except ValueError:
            print("Annual salary should contain number.")
    # validate bonus loop
    loop_flag = True
    while loop_flag:
        ann_bonus = input("Enter ShiftSupervisor's annual bonus: ")
        try:
            ann_bonus = float(ann_bonus)
            loop_flag = False
        except ValueError:
            print("Annual salary should contain number.")
    # make object from subclass ProductionWorker
    supervisor = ShiftSupervisor(name, number, ann_salary, ann_bonus)
    print(f"ShiftSupervisor's name: {supervisor.get_name()}")
    print(f"ShiftSupervisor's number: {supervisor.get_number()}")
    print(f"ShiftSupervisor's annual salary: ${supervisor.get_ann_salary()}")
    print(f"ShiftSupervisor's annual bonus: ${supervisor.get_ann_bonus()}")


# Call the main function.
if __name__ == '__main__':
    main()
