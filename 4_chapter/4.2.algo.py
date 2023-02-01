continue_flag = 'да'
while continue_flag == 'да' or continue_flag == 'Да' or continue_flag == 'ДА' or continue_flag == 'д' or continue_flag == 'Д':
    number1 = float (input ('Введите первое число: '))
    number2 = float (input ('Введите второе число: '))
    print(f'Сумма введённых чисел равна {number1 + number2}')
    continue_flag = input ('Повторить вычисление ещё раз (да/нет)? ')
print('конец цикла')