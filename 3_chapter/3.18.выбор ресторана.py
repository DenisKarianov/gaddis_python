# программа помогает выбрать ресторан

# устанавливаем имен.константы диет ресторанов
JO_VEGETERIAN = False
JO_VEGAN = False
JO_WITHOUT_GLUTEN = False
CENTAL_PIZZERIA_VEGETERIAN = True
CENTAL_PIZZERIA_VEGAN = False
CENTAL_PIZZERIA_WITHOUT_GLUTEN = True
CAFE_VEGETERIAN = True
CAFE_VEGAN = True
CAFE_WITHOUT_GLUTEN = True
DISHES_ITALIAN_VEGETERIAN = True
DISHES_ITALIAN_VEGAN = False
DISHES_ITALIAN_WITHOUT_GLUTEN = False
KITCHEN_VEGETERIAN = True
KITCHEN_VEGAN = True
KITCHEN_WITHOUT_GLUTEN = True

# спрашиваем про диетические предпочтения и устанавливаем соответствующий флаг
vegetarian = input ('Будет ли на ужине вегетарианец (да/нет)? ')
if vegetarian == 'да' or vegetarian == 'Да' or vegetarian == 'ДА' or vegetarian == 'дА':
    vegetarian_flag = True
else:
    vegetarian_flag = False
vegan = input ('Будет ли на ужине веганец (да/нет)? ')
if vegan == 'да' or vegan == 'Да' or vegan == 'ДА' or vegan == 'дА':
    vegan_flag = True
else:
    vegan_flag = False
bezgluten = input ('Будет ли на ужине приверженец безглютеновой диеты (да/нет)? ')
if bezgluten == 'да' or bezgluten == 'Да' or bezgluten == 'ДА' or bezgluten == 'дА':
    bezgluten_flag = True
else:
    bezgluten_flag = False

print ('Вот ваши варианты ресторанов:')
# определяем идём ли в гамбургеры Джо
# определяемся по вегетарианцам
if vegetarian_flag:
    if JO_VEGETERIAN:
        jo_go_vegetarian = True
    else:
        jo_go_vegetarian = False
else:
    jo_go_vegetarian = True

# определяемся по веганам
if vegan_flag:
    if JO_VEGAN:
        jo_go_vegan = True
    else:
        jo_go_vegan = False
else:
    jo_go_vegan = True

# определяемся по безглютенам
if bezgluten_flag:
    if JO_WITHOUT_GLUTEN:
        jo_go_without_gluten = True
    else:
        jo_go_without_gluten = False
else:
    jo_go_without_gluten = True

# окончательно определяем идем ли в гамбургеры Джо, если да, то вывод названия ресторана
if jo_go_vegetarian and jo_go_vegan and jo_go_without_gluten:
    print ('Изысканные гамбургеры от Джо')

# определяем идём ли в Центральную пиццерию
# определяемся по вегетарианцам
if vegetarian_flag:
    if CENTAL_PIZZERIA_VEGETERIAN:
        cental_pizzeria_go_vegetarian = True
    else:
        cental_pizzeria_go_vegetarian = False
else:
    cental_pizzeria_go_vegetarian = True

# определяемся по веганам
if vegan_flag:
    if CENTAL_PIZZERIA_VEGAN:
        cental_pizzeria_go_vegan = True
    else:
        cental_pizzeria_go_vegan = False
else:
    cental_pizzeria_go_vegan = True

# определяемся по безглютенам
if bezgluten_flag:
    if CENTAL_PIZZERIA_WITHOUT_GLUTEN:
        cental_pizzeria_go_without_gluten = True
    else:
        cental_pizzeria_go_without_gluten = False
else:
    cental_pizzeria_go_without_gluten = True

# окончательно определяем идем ли в Центральную пиццерию, если да, то вывод названия ресторана
if cental_pizzeria_go_vegetarian and cental_pizzeria_go_vegan and cental_pizzeria_go_without_gluten:
    print ('Центральная пиццерия')

# определяем идём ли в Кафе за углом
# определяемся по вегетарианцам
if vegetarian_flag:
    if CAFE_VEGETERIAN:
        cafe_go_vegetarian = True
    else:
        cafe_go_vegetarian = False
else:
    cafe_go_vegetarian = True

# определяемся по веганам
if vegan_flag:
    if CAFE_VEGAN:
        cafe_go_vegan = True
    else:
        cafe_go_vegan = False
else:
    cafe_go_vegan = True

# определяемся по безглютенам
if bezgluten_flag:
    if CAFE_WITHOUT_GLUTEN:
        cafe_go_without_gluten = True
    else:
        cafe_go_without_gluten = False
else:
    cafe_go_without_gluten = True

# окончательно определяем идем ли в Кафе за углом, если да, то вывод названия ресторана
if cafe_go_vegetarian and cafe_go_vegan and cafe_go_without_gluten:
    print ('Кафе за углом')

# определяем идём ли в Блюда от итальянской мамы
# определяемся по вегетарианцам
if vegetarian_flag:
    if DISHES_ITALIAN_VEGETERIAN:
        dishes_italian_go_vegetarian = True
    else:
        dishes_italian_go_vegetarian = False
else:
    dishes_italian_go_vegetarian = True

# определяемся по веганам
if vegan_flag:
    if DISHES_ITALIAN_VEGAN:
        dishes_italian_go_vegan = True
    else:
        dishes_italian_go_vegan = False
else:
    dishes_italian_go_vegan = True

# определяемся по безглютенам
if bezgluten_flag:
    if DISHES_ITALIAN_WITHOUT_GLUTEN:
        dishes_italian_go_without_gluten = True
    else:
        dishes_italian_go_without_gluten = False
else:
    dishes_italian_go_without_gluten = True

# окончательно определяем идем ли в Блюда от итальянской мамы, если да, то вывод названия ресторана
if dishes_italian_go_vegetarian and dishes_italian_go_vegan and dishes_italian_go_without_gluten:
    print ('Блюда от итальянской мамы')
    
# определяем идём ли в Кухню шеф-повара
# определяемся по вегетарианцам
if vegetarian_flag:
    if KITCHEN_VEGETERIAN:
        kitchen_go_vegetarian = True
    else:
        kitchen_go_vegetarian = False
else:
    kitchen_go_vegetarian = True

# определяемся по веганам
if vegan_flag:
    if KITCHEN_VEGAN:
        kitchen_go_vegan = True
    else:
        kitchen_go_vegan = False
else:
    kitchen_go_vegan = True

# определяемся по безглютенам
if bezgluten_flag:
    if KITCHEN_WITHOUT_GLUTEN:
        kitchen_go_without_gluten = True
    else:
        kitchen_go_without_gluten = False
else:
    kitchen_go_without_gluten = True

# окончательно определяем идем ли в Кухню шеф-повара, если да, то вывод названия ресторана
if kitchen_go_vegetarian and kitchen_go_vegan and kitchen_go_without_gluten:
    print ('Кухня шеф-повара')