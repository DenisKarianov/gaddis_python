# очки за купленные книги

# запрашиваем у пользователя количество купленных книг в этом месяце
book_quantity = int (input('Введите количество книг, купленных в этом месяце: '))

# сообщаем о выигрыше
if book_quantity == 0 or book_quantity == 1:
    print ('Вы не заработали очки в этом месяце.')
elif book_quantity == 2 or book_quantity == 3:
    print ('Вы заработали 5 очков в этом месяце.')
elif book_quantity == 4 or book_quantity == 5:
    print ('Вы заработали 15 очков в этом месяце.')
elif book_quantity == 6 or book_quantity == 7:
    print ('Вы заработали 30 очков в этом месяце.')
elif book_quantity >= 8:
    print ('Вы заработали 60 очков в этом месяце.')
else:
    print ('Ошибка. Пожалуйста, проверьте введённое число купленных книг.')