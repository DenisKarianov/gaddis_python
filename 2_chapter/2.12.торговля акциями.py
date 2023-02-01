# программа расчёта прибыли(убытков) от торговли акциями

# объявляем именованные константы
PURCHASED_SHARES_NUMBER = 2000
PURCHASE_PRICE = 40.00
PURCHASE_FEE = 0.03
SOLD_SHARES_NUMBER = 2000
SOLD_PRICE = 42.75
SOLD_FEE = 0.03

# вывод расчётов
print (f'За покупку акций уплачено: {PURCHASED_SHARES_NUMBER*PURCHASE_PRICE:.2f} долларов.')
print (f'Размер комиссии брокера при покупке акций: {PURCHASED_SHARES_NUMBER*PURCHASE_PRICE*PURCHASE_FEE:.2f} долларов.')
print (f'От продажи акций получено: {SOLD_SHARES_NUMBER*SOLD_PRICE:.2f} долларов.')
print (f'Размер комиссии брокера при покупке акций: {SOLD_SHARES_NUMBER*SOLD_PRICE*SOLD_FEE:.2f} долларов.')
print (f'Результат торговли акциями: {SOLD_SHARES_NUMBER*SOLD_PRICE-(PURCHASED_SHARES_NUMBER*PURCHASE_PRICE+PURCHASED_SHARES_NUMBER*PURCHASE_PRICE*PURCHASE_FEE+SOLD_SHARES_NUMBER*SOLD_PRICE*SOLD_FEE):.2f} долларов.')