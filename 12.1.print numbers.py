# function to print numbers from 1 to n by using recursion

def main():
    n = 14
    print_numb(n)


def print_numb(n):
    if n > 1:
        print_numb(n - 1)
    print(n, end=' ')


# Call the main function.
if __name__ == '__main__':
    main()
