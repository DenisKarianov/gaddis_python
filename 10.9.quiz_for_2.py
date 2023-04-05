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
    questions2 = []  # list for objects
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
    pl_points = [0] * PLAYERS_QUANT  # list to count all participants' points
    partic_counter = 0  # list to count participants
    for i, q in enumerate(questions):
        if i == 0:
            print(f"Вопросы для участника {players_names[i]}:")
        elif i % 5 == 0:  # questions for every participant after first one (5 questions for each one)
            partic_counter += 1  # new participant after every 5 questions
            print()
            print("Внимание!")
            print(f"Вопросы для участника {players_names[partic_counter]}:")
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
        if int(number) == q.get_number():
            pl_points[partic_counter] += 1
    # print quantity correct answers for each player
    for i, n in enumerate(players_names):
        print(f"Количество правильных ответов участника {n}: {pl_points[i]}")
    # get winners' list indexes
    winners = [i for i, x in enumerate(pl_points) if x == max(pl_points)]
    # print winners' names
    if len(winners) == 1:
        print(f"Выиграл игрок {players_names[winners[0]]}")
    else:
        print("Победители:")
        for i in winners:
            print(players_names[i])


# Call the main function.
if __name__ == '__main__':
    main()
