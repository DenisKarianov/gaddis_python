# программа расчёта калорий из жиров и углеводов

# глобальные константы
FAT_RATE = 9  # коэффициент жиров
CARBOHYDRATE_RATE = 4  # коэффициент углеводов
DECIMAL_PLACES = 2 # количество знаков в десятичной дробив (после запятой)

def main():
    # запрос данных у пользователя
    fat = float (input ("Введите количество употреблённых жиров в граммах: "))
    carbohydrate = float (input ("Введите количество употреблённых углеводов в граммах: "))
    # вызов функции расчёта и показа калорий
    show_kal(fat, carbohydrate) 
        
def show_kal(fat, carbohydrate):
    calories_consumed_fat = fat * FAT_RATE
    calories_consumed_carbohydrate = carbohydrate * CARBOHYDRATE_RATE
    print (f'Вы употребили {calories_consumed_fat + calories_consumed_carbohydrate} калорий.')
    
main()