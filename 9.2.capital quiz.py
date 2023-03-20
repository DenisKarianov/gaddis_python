# world's capital quiz

# import pandas to read data from xls-file
import pandas as pd
# import random for random choices of questions
import random

FILE = 'countries.xlsx'
# convert xlsx-file to dataframe
infile = pd.ExcelFile(FILE)
data = infile.parse(infile.sheet_names[0])
# make dict - 'Country' column - key, 'Capital' column - value
capital_countries1 = dict(zip(data.Country, data.Capital))
# make list of known countries
infile2 = pd.ExcelFile('known_countries.xlsx')
data2 = infile2.parse(infile2.sheet_names[0])
countries2 = list(data2.Страна)
# make shorted dict of countries and capitals
capital_countries2 = {country: capital_countries1[country] for country in capital_countries1 if country in countries2}

def main():
    players_quant = int(input("Введите количество участников: "))
    players_names = []
    for i in range(players_quant):
        players_names.append(input(f"Введите имя участника № {i + 1}: "))
    quest_quant = int(input("Введите количество вопросов: "))
    print("Выберите уровень сложности")
    diff_level = int(input('Лёгкий уровень - введите "1", сложный уровень - введите "2": '))
    print("Викторина началась!")
    if diff_level == 1:
        quiz(players_quant, players_names, quest_quant, capital_countries2)
    else:
        quiz(players_quant, players_names, quest_quant, capital_countries1)



def quiz(players_quant, players_names, quest_quant, dictionary):
    # adapt dict name for program - define difficulty level
    capital_countries = dictionary
    # make list of keys to get random questions
    countries_list = list(capital_countries)
    # make list for answers
    all_answers = []
    # make list for questions
    all_quest = []
    for p in range(players_quant):
        # create answer's list for each player
        pl_answers = []
        # create question's list for each player
        pl_quest = random.sample(countries_list, k=quest_quant)
        # save lists of questions to common 2d-list
        all_quest.append(pl_quest)
        print(f"Вопросы для игрока {players_names[p]}:")
        for q in range(quest_quant):
            print(f"Вопрос № {q + 1}")
            answ = input(f"Назовите столицу страны {pl_quest[q]}: ")
            pl_answers.append(answ)
        # save lists of answers to common 2d-list
        all_answers.append(pl_answers)
    # check and count results
    # make a mask to check results
    all_results = []
    # list to count correct answers
    count_results = [0] * players_quant
    for p in range(players_quant):
        # results' list for each player
        pl_results = []
        for q in range(quest_quant):
            if capital_countries[all_quest[p][q]].upper() == all_answers[p][q].upper():
                pl_results.append(True)
                count_results[p] += 1
            else:
                pl_results.append(False)
        # save results in common results' list
        all_results.append(pl_results)
    # get winners' list indexes
    winners = [i for i, x in enumerate(count_results) if x == max(count_results)]
    # print winners' names
    if len(winners) == 1:
        print(f"Выиграл игрок {players_names[winners[0]]}")
    else:
        print("Победители:")
        for i in winners:
            print(players_names[i])
    # print results
    print("Результаты")
    print("------------------")
    # variables for table
    name = "Имя"
    correct_quant = "Верные ответы"
    wrong_quant = "Неверные ответы"
    print(f"{name:^10}\t{correct_quant:^10}\t{wrong_quant:^10}")
    # sort players for results and print
    count_results2 = [] + count_results
    min_value = min(count_results2)
    for i in count_results2:
        # condition to avoid removed results
        if max(count_results2) >= min_value:
            print(f"{players_names[count_results2.index(max(count_results2))]:^10}\t{max(count_results2):^10}\t"
                  f"{quest_quant - max(count_results2):^10}")
            # remove max value to get the next one on next iteration
            count_results2[count_results2.index(max(count_results2))] = - 1
    # print wrong and correct answers for each player
    for p in range(players_quant):
        print(f"Разбираем ответы игрока {players_names[p]}")
        # condition if all answers are correct
        if all(all_results[p]):
            print(f"Все ответы игрока {players_names[p]} верны.")
        else:
            # variables for table
            country = "Страна"
            play_answ = "Ответ участника"
            correct_answ = "Верный ответ"
            print(f"{country:^6}\t{play_answ:^15}\t{correct_answ:^12}")
            for q in range(quest_quant):
                # condition for wrong answer
                if not all_results[p][q]:
                    print(f"{all_quest[p][q]:^6}\t{all_answers[p][q]:^15}\t{capital_countries[all_quest[p][q]]:^12}")


# Call the main function.
if __name__ == '__main__':
    main()
