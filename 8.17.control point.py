# loop to count uppercase symbols in string

mystring = 'abcDEFG'
uppercase_total = 0
for ch in mystring:
    if ch.isupper():
        uppercase_total += 1
print(f'Quantity of uppercase symbols in {mystring}: {uppercase_total}.')