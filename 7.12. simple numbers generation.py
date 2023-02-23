# make prime number list from user number

def is_prime(number):
    if number % 1 == 0 and number > 2:  # define if number is whole and > 2
        composite_number_flag = 0  # declare a variable for composite number flag
        counter = number - 1  # declare decreasing divisor, that check number for composite
        while composite_number_flag == 0 and counter > 1:
            if number % counter == 0:
                composite_number_flag += 1
            else:
                counter -= 1
        if composite_number_flag == 0:
            status = True
        else:
            status = False
    elif number == 2:
        status = True
    else:
        status = False
    return status


def main():
    try:
        user_number = int(input("Enter integer number > 1: "))
        # check if entered number > 1
        if user_number > 1:
            # make list of integer numbers from 2 till entered number
            int_list = []
            for number in range(2, user_number + 1):
                int_list.append(number)
            # make list of prime numbers from list of integer numbers
            prime_list = [number for number in int_list if is_prime(number)]
            # print prime numbers
            for number in prime_list:
                print(f'{number}', end=' ')
        else:
            print("Number should be > 1.")
    except ValueError:
        print("Number should be integer and > 1.")


# Call the main function.
if __name__ == '__main__':
    main()
