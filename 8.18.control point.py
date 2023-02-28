# make list from string

some_string = 'Monday Tuesday Wednesday'
string_list = some_string.split()
print(string_list)

# 8.19 control point
second_string = 'one$two$three$four'
string_list2 = second_string.split('$')
print(string_list2)

# 8.2 algo: count space quantity in string
mystring = 'tree day week lunch'
total = 0
for ch in mystring:
    if ch == ' ':
        total += 1
print(f'Spaces quantity: {total}')

# 8.3 algo:  count number quantity in string
mystring = 'tree 3day week lunch 434'
total = 0
for ch in mystring:
    if ch.isdigit():
        total += 1
print(f'Number quantity: {total}')

# 8.4 algo:  count lowercase symbols in string
mystring = 'Tree 3day week lUnch 434'
total = 0
for ch in mystring:
    if ch.islower():
        total += 1
print(f'Lowercase symbols quantity: {total}')

# 8.5 algo:  function returns True if there is '.com' in the end of the string
def find_com(string):
    if string.endswith('.com'):
        status = True
    else:
        status = False
    return status

print(find_com('tesla.com'))

# 8.6 algo:  make copy of string with replacement of lowercase 't' to 'T'
t_string = 'tree twelve travel test tasty'
uppercase_t_string = t_string.replace('t', 'T')
print(uppercase_t_string)

# 8.8. algo: instruction that print first 3 symbols in string
mystring = 'etewf3k'
print(mystring[0:3])

# 8.9. algo: instruction that print last 3 symbols in string
mystring = 'etewf3k'
print(mystring[-3:])

# 8.10. algo: instruction that split string and print list
mystring = 'pies>milk>meal>apple pie>icecream'
str_list3 = mystring.split('>')
print(str_list3)


