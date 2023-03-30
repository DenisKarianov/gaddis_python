# program to create an object from class RetailItem


def main():
    # make class RetailItem with some data
    class RetailItem:
        def __init__(self, name, quant, price):
            self.__name = name
            self.__quant = quant
            self.__price = price

        def set_name(self, name):
            self.__name = name

        def set_quant(self, quant):
            self.__quant = quant

        def set_price(self, price):
            self.__price = price


        def get_name(self):
            return self.__name

        def get_quant(self):
            return self.__quant

        def get_price(self):
            return self.__price


        def __str__(self):
            return f"Name: {self.__name}\n" + \
                   f"Quantity in stock: {self.__quant}\n" + \
                   f"Price: {self.__price}\n"

    # create 3 objects from class RetailItem
    ret_item1 = RetailItem("Coat", 12, 59.95)
    ret_item2 = RetailItem("Designer jeans", 40, 34.95)
    ret_item3 = RetailItem("Shirt", 20, 24.95)
    # print objects' data
    print(ret_item1)
    print()
    print(ret_item2)
    print()
    print(ret_item3)


# Call the main function.
if __name__ == '__main__':
    main()
