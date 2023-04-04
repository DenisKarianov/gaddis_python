# make class question for quiz
class Question:
    def __init__(self, quest, answer1, answer2, answer3, answer4, corr_answ_number):
        self.__quest = quest
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__corr_answ_number = corr_answ_number

    def set_quest(self, quest):
        self.__quest = quest

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_number(self, corr_answ_number):
        self.__corr_answ_number = corr_answ_number

    def get_quest(self):
        return self.__quest

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_number(self):
        return self.__corr_answ_number