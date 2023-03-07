# program to divide words in string


def main():
    # get data from user
    user_data = input('Please, enter a string: ')
    print(f'{divide_words(user_data)}')


def divide_words(in_string):
    # variable to count iterations
    loop_counter = 0
    # empty list to save words
    words_list = []
    for ch in in_string:
        if 0 < loop_counter < (len(in_string) - 1):  # for all characters except first and last
            if ch.isupper():
                words_list.append(str1)
                str1 = ''
                str1 += ch.lower()
                loop_counter += 1
            else:
                str1 += ch
                loop_counter += 1
        elif loop_counter == len(in_string) - 1:  # for last character
            if ch.isupper():
                words_list.append(str1)
                str1 = ''
                str1 += ch.lower()
                words_list.append(str1)
                loop_counter += 1
            else:
                str1 += ch
                words_list.append(str1)
                loop_counter += 1
        else:  # for first character
            str1 = ''
            str1 += ch.upper()
            loop_counter += 1
    # make result string
    result_string = ''
    for word in words_list:
        result_string += word
        result_string += ' '
    return result_string


# Call the main function.
if __name__ == '__main__':
    main()
