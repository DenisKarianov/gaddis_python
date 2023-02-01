# расчёт стоимости покупки товаров
# ввод цен товаров
product1 = int (input ("Введите цену первого товара и нажмите 'Enter': "))
product2 = int (input ("Введите цену второго товара и нажмите 'Enter': "))
product3 = int (input ("Введите цену третьего товара и нажмите 'Enter': "))
product4 = int (input ("Введите цену четвёртого товара и нажмите 'Enter': "))
product5 = int (input ("Введите цену пятого товара и нажмите 'Enter': "))

# расчёт общей стоимости товаров
product_all = product1+product2+product3+product4+product5

# вывод на печать суммы к оплате с учётом налога с продаж 7%
print (f'Итоговая сумма к оплате составляет: {product_all+product_all*0.07:.2f}')