# калькулятор сосисок и булочек для пикника

# запрашиваем количество участников пикника у пользователя
participant_number = int(input('Введите количество участников пикника: '))

# запрашиваем количество хот-догов для каждого участника
# пикника у пользователя
hotdog_number = float(input('Введите количество хот-догов для каждого участника: '))

# устанавливаем именнованные константы для количества сосисок и булочек
# в упаковке
SAUSAGE_PACKAGE = 10
BUN_PACKAGE = 8

# вычисляем необходимое количество упаковок сосисок и определяем,
# есть ли остатки
if participant_number*hotdog_number%SAUSAGE_PACKAGE != 0: # проверяю наличие остатка
    sausage_package_number = participant_number * hotdog_number // SAUSAGE_PACKAGE + 1
    sausage_package_remainder = sausage_package_number * SAUSAGE_PACKAGE - participant_number*hotdog_number
else:
    sausage_package_number = participant_number * hotdog_number // SAUSAGE_PACKAGE
    sausage_package_remainder = 0

# вычисляем необходимое количество упаковок булочек и определяем,
# есть ли остатки
if participant_number*hotdog_number%BUN_PACKAGE != 0: # проверяю наличие остатка
    bun_package_number = participant_number * hotdog_number // BUN_PACKAGE + 1
    bun_package_remainder = bun_package_number * BUN_PACKAGE - participant_number*hotdog_number
else:
    bun_package_number = participant_number * hotdog_number // BUN_PACKAGE
    bun_package_remainder = 0

print (f'Необходимо {int(sausage_package_number)} упаковок сосисок.')
print (f'Необходимо {int(bun_package_number)} упаковок булочек.')
print (f'Останется {sausage_package_remainder:.1f} сосисок.')
print (f'Останется {bun_package_remainder:.1f} булочек.')