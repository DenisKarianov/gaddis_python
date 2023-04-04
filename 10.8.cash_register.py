# program to create an object from class Employee

import retail_cash_class as retail

# global constants for menu items
ADD = 1
SHOW = 2
QUIT = 3


def main():
    # make basket
    basket = retail.CashRegister()
    choice = 0  # variable for user's menu item's choice
    while choice != QUIT:
        choice = get_menu_choice()  # get menu item from user
        # realise chosen item
        if choice == 1:
            add(basket)
        elif choice == 2:
            show(basket)
    print("Goodbye!")


def get_menu_choice():
    print()
    print("Menu")
    print("-------------------")
    print("1. Add goods")
    print("2. Show goods")
    print("3. Quit")
    print()
    # get item from user and validate it
    loop_flag = 0  # variable for loop control
    while loop_flag < 2:
        loop_flag = 0  # erase for new iteration
        # get menu item from user
        choice = input("Enter chosen menu item: ")
        if choice.isdigit():
            loop_flag += 1
            choice_int = int(choice)
            if 1 <= choice_int <= 3:
                loop_flag += 1
    return choice_int


def add(basket):
    name = input("Enter goods' name: ")
    loop_flag = True  # flag for validation loop
    while loop_flag:
        quant = input("Enter goods' quantity: ")
        if is_int(quant):
            quant = int(quant)
            loop_flag = False
    loop_flag2 = True  # flag for second validation loop
    while loop_flag2:
        price = input("Enter goods' price: ")
        if is_float(price):
            price = float(price)
            loop_flag2 = False
    # make object  from class Retail_item form user's data
    goods = retail.RetailItem(name, quant, price)
    # add goods to basket
    basket.purchase_item(goods)


def show(basket):
    basket.show_items()
    print(f"Total value: ${basket.get_total()}")


def is_int(str1):
    try:
        int(str1)
        return True
    except ValueError:
        return False


def is_float(str1):
    try:
        float(str1)
        return True
    except ValueError:
        return False


# Call the main function.
if __name__ == '__main__':
    main()
