# program to check if account's number is acceptable by comparison
# with list in file charge_accounts.txt

def main():
    infile = open('charge_accounts.txt', 'r') # open file for reading
    acceptable_accounts = infile.readlines() # input file content to list
    infile.close()
    # remove '\n'
    index = 0
    while index < len(acceptable_accounts):
        acceptable_accounts[index] = acceptable_accounts[index].rstrip('\n')
        index += 1
    user_account = input('Enter your account number: ') # get account number from user
    # check if user account is in list
    if user_account in acceptable_accounts:
        print('Account number is acceptable.')
    else:
        print('Account number is unacceptable.')


# Call the main function.
if __name__ == '__main__':
    main()
