# program to remake sentence to youth jargon - first letter to the end plus 'ki'


def main():
    # get data from user
    user_data = input('Please, enter a sentence: ')
    print(f'{youth_jargon(user_data)}')


def youth_jargon(in_string):
    # empty list to save words
    words_list = []
    # empty list to save jargon words
    jargon_list = []
    # empty string to separate words
    str1 = ''
    index1 = 0
    while index1 < len(in_string):
        if index1 < (len(in_string) - 1):
            if in_string[index1] == ' ' or in_string[index1] == '  ' or in_string[index1] == '   ':
                words_list.append(str1)
                str1 = ''
                index1 += 1
            else:
                str1 += in_string[index1]
                index1 += 1
        else:
            str1 += in_string[index1]
            words_list.append(str1)
            index1 += 1
    # make jargon words
    for word in words_list:
        index = 0
        str2 = ''
        while index < len(word):
            if index == 0:
                first_char = word[index]
                index += 1
            elif 0 < index < (len(word) - 1):
                str2 += word[index]
                index += 1
            else:  # add first character and ki in the word's end
                str2 += word[index]
                str2 += first_char
                str2 += 'ki'
                index += 1
        jargon_list.append(str2)
    # make result string
    result_string = ''
    for word in jargon_list:
        result_string += word
        result_string += ' '
    return result_string


# Call the main function.
if __name__ == '__main__':
    main()
