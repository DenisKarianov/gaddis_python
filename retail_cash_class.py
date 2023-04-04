# make class RetailItem and CashRegister
class RetailItem:
    def __init__(self, name, quant, price):
        self.__name = name  # product description
        self.__quant = quant  # product quantity
        self.__price = price  # product price

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


class CashRegister:
    def __init__(self):
        self.__items = []

    def purchase_item(self, retail_item):
        self.__items.append(retail_item)

    def get_total(self):
        total = 0.0
        for item in self.__items:
            total += item.get_price() * item.get_quant()
        return total

    def show_items(self):
        product = "Product"
        quant = "Quantity"
        price = "Price"
        amount = "Amount"
        print(f"{product:^10}\t{quant:^8}\t{price:^5}\t{amount:^6}")
        for item in self.__items:
            print(f"{item.get_name():^10}\t{item.get_quant():^8}\t{item.get_price():^5}\t"
                  f"{item.get_price() * item.get_quant():^6}")

    def clear(self):
        self.__items = []
