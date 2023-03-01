# program to correct sentence for uppercase letters in start of sentences instead of lowercase


def main():
    # get string with sentences from user
    user_data = input('Please, enter a sentences: ')
    print(make_uppercase(user_data))


def make_uppercase(str1):
    # loop counter
    counter = 0
    # modified string
    str2 = ''
    # flag for sentence's end
    end_flag = False
    while counter < len(str1):
        if counter == 0 and str1[counter].islower():
            str2 += str1[counter].upper()
            counter += 1
        else:
            if end_flag:
                if str1[counter].isalnum():
                    if str1[counter].isalpha():
                        if str1[counter].isupper():
                            str2 += str1[counter]
                            end_flag = False
                            counter += 1
                        else:
                            str2 += str1[counter].upper()
                            end_flag = False
                            counter += 1
                    else:
                        str2 += str1[counter]
                        end_flag = False
                        counter += 1
                else:
                    str2 += str1[counter]
                    counter += 1
            else:
                if str1[counter] == '.' or str1[counter] == '!' or str1[counter] == '?':
                    str2 += str1[counter]
                    end_flag = True
                    counter += 1
                else:
                    str2 += str1[counter]
                    counter += 1
    return str2


# Call the main function.
if __name__ == '__main__':
    main()
