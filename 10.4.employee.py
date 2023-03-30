# program to create an object from class Employee

import employee

def main():
    # create 3 objects from class Employee
    emp1 = employee.Employee("Susan Mayers", "47899", "Accounting", "Vice president")
    emp2 = employee.Employee("Mark Jones", "39119", "IT", "Developer")
    emp3 = employee.Employee("Joy Rogers", "81774", "Production", "Engineer")
    # print objects' data
    print(emp1)
    print()
    print(emp2)
    print()
    print(emp3)


# Call the main function.
if __name__ == '__main__':
    main()
