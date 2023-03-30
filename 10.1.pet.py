# program to create an object from class Pet

import pet


def main():
    # get info about pet from user
    name = input("Enter pet's name: ")
    animal_type = input("Enter pet's animal type: ")
    age = input("Enter pet's age: ")
    # create an object from class Pet using user's info
    pet1 = pet.Pet(name, animal_type, age)
    # print info about pet from created object by using object's method
    print(f"Pet's name: {pet1.get_name()}")
    print(f"Pet's animal type: {pet1.get_animal_type()}")
    print(f"Pet's age: {pet1.get_age()}")


# Call the main function.
if __name__ == '__main__':
    main()
