# program to create initials from full name

def main():
    # get name from user
    full_name = input('Please, enter your full name, divided by spaces: ')
    for name in full_name.split():
        print(name[0].upper() + '.', end='')


# Call the main function.
if __name__ == '__main__':
    main()
