# quiz for 2 participants

# import pandas to read data from xls-file
import pandas as pd
# import random for random choices of questions
import random
# import class Question
import question_class as qstn

# global constants
PLAYERS_QUANT = 2  # quantity of players
FILE = 'quiz2.xlsx'


def main():
    # convert xlsx-file to dataframe
    infile = pd.ExcelFile(FILE)
    data = infile.parse(infile.sheet_names[0])
    qlist = data.values.tolist()  # make 2d-list with data for quiz
    # make list with objects at random
    questions = random.sample(qlist, k=PLAYERS_QUANT * 5)  # 2d-list with random questions
    questions2 = []
    for q in questions:
        # make object from class Question
        quest_obj = qstn.Question(q[0], q[1], q[2], q[3], q[4], q[5])
        questions2.append(quest_obj)  # add object to list
    players_names = []
    for i in range(PLAYERS_QUANT):
        players_names.append(input(f"Введите имя участника № {i + 1}: "))
    print("Викторина началась!")
    quiz(PLAYERS_QUANT, players_names, questions2)


def quiz(players_quant, players_names, questions):
    pl_points = []  # list to count players' points
    for i, q in enumerate(questions):
        if i == 0 or i == 5:
            print(f"Вопросы для участника {players_names[i]}:")
        print(f"{q.get_quest()}")
        print("Варианты ответов:")
        print(f"1. {q.get_answer1()}")
        print(f"2. {q.get_answer2()}")
        print(f"3. {q.get_answer3()}")
        print(f"4. {q.get_answer4()}")
        loop_flag = 0  # flag for validation loop
        while loop_flag < 2:
            loop_flag = 0  # erase for each iteration
            number = input("Введите ваш вариант ответа (число от 1 до 4): ")
            if number.isdigit():
                loop_flag += 1
                if 1 <= int(number) <= 4:
                    loop_flag += 1



    for p in range(players_quant):
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
