# count feet to inches

# global constants
FED_TAX_RATE = 0.05
MUN_TAX_RATE = 0.025


def main():
    # ask user for feet quantity
    feet = float(input('Please input feet quantity: '))
    # call for count inches function and print
    print(f'{feet} feet is {feet_to_inches(feet):.1f} inches.')


def feet_to_inches(feet):
    return feet * 12


main()
