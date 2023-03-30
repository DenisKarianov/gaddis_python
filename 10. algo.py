# class Bool

class Book:
    def __init__(self, header, author_name, publ_name):
        self.__header = header
        self.__author_name = author_name
        self.__publ_name = publ_name

    def set_header(self, header):
        self.__header = header

    def set_author_name(self, author_name):
        self.__author_name = author_name

    def set_publ_name(self, publ_name):
        self.__publ_name = publ_name

    def get_header(self):
        return self.__header

    def get_author_name(self):
        return self.__author_name

    def get_publ_name(self):
        return self.__publ_name

    def __str__(self):
        return f'Header: {self.__header}' + \
               f'Author: {self.__author_name}' + \
               f'Publisher: {self.__publ_name}'
