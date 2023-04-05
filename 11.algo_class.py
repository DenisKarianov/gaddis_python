# make base class Beverage and subclass Cola
class Beverage:
    def __init__(self, bev_name):
        self.__bev_name = bev_name


class Cola(Beverage):
    def __init__(self):
        Beverage.__init__(self, 'Coca-Cola')
