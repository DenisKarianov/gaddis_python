# program read steps quantity from file and count average quantity for every month.

# global constants
FILE_NAME = 'steps.txt'

def main():
    input_file = open(FILE_NAME, 'r')  # open a file for reading
    counter = 0  # declare variable to count days
    january_steps = 0
    february_steps = 0
    march_steps = 0
    april_steps = 0
    may_steps = 0
    june_steps = 0
    july_steps = 0
    august_steps = 0
    september_steps = 0
    october_steps = 0
    november_steps = 0
    december_steps = 0
    for line in input_file:
        counter += 1
        if 1 <= counter <= 31:
            january_steps += int(line)
        elif 32 <= counter <= 59:
            february_steps += int(line)
        elif 30 <= counter <= 90:
            march_steps += int(line)
        elif 91 <= counter <= 120:
            april_steps += int(line)
        elif 121 <= counter <= 151:
            may_steps += int(line)
        elif 152 <= counter <= 181:
            june_steps += int(line)
        elif 182 <= counter <= 212:
            july_steps += int(line)
        elif 213 <= counter <= 243:
            august_steps += int(line)
        elif 244 <= counter <= 273:
            september_steps += int(line)
        elif 274 <= counter <= 304:
            october_steps += int(line)
        elif 305 <= counter <= 334:
            november_steps += int(line)
        elif 335 <= counter <= 365:
            december_steps += int(line)
    input_file.close()
    print(f'{january_steps / 31:.0f} steps were taken in January every day in average.')
    print(f'{february_steps / 28:.0f} steps were taken in February every day in average.')
    print(f'{march_steps / 31:.0f} steps were taken in March every day in average.')
    print(f'{april_steps / 30:.0f} steps were taken in April every day in average.')
    print(f'{may_steps / 31:.0f} steps were taken in May every day in average.')
    print(f'{june_steps / 30:.0f} steps were taken in June every day in average.')
    print(f'{july_steps / 31:.0f} steps were taken in July every day in average.')
    print(f'{august_steps / 31:.0f} steps were taken in August every day in average.')
    print(f'{september_steps / 30:.0f} steps were taken in September every day in average.')
    print(f'{october_steps / 31:.0f} steps were taken in October every day in average.')
    print(f'{november_steps / 30:.0f} steps were taken in November every day in average.')
    print(f'{december_steps / 31:.0f} steps were taken in December every day in average.')


main()
