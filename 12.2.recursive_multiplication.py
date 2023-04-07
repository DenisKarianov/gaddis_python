# function to multiply two numbers by using recursion
# these numbers are integer and > 0

def main():
    x = 14
    y = 5
    print(multiply(x, y))


def multiply(x, y):
    if x == 1:
        return y
    else:
        return y + multiply(x - 1, y)



# Call the main function.
if __name__ == '__main__':
    main()
