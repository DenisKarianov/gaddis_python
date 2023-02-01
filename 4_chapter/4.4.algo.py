total = 0.0
for number in range (1, 31):
    result = number / (31 - number)
    total += result
print (f'{total:.2f}')