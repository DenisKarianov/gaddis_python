# program to create an object from class Car

import class_car as car

# global constants
YEAR_MODEL = "C4 2020"
MAKE = "Citroen"


def main():
    # create an object from class Car
    car1 = car.Car(YEAR_MODEL, MAKE)
    # use accelerate method 5 times and print speed
    for i in range(5):
        car1.accelerate()
        print(f"Speed: {car1.get_speed()}")
    for i in range(5):
        car1.brake()
        print(f"Speed: {car1.get_speed()}")


# Call the main function.
if __name__ == '__main__':
    main()
