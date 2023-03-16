# program to make dictionaries for studying courses

# make dict with course # and room
rooms = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'CS104': '1244', 'CS105': '1411'}
# make dict with course # and professor's name
names = {'CS101': 'Hines', 'CS102': 'Alvarado', 'CS103': 'Rich', 'CS104': 'Berk', 'CS105': 'Lee'}
# make dict with course # and beginning time
times = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'CS104': '11:00', 'CS105': '13:00'}

def main():
    # get data from user
    user_data = input('Please, enter a course number: ')
    print_course_info(user_data)


def print_course_info(in_string):
    # check if entered course number is in dict
    if in_string.upper() in rooms:
        print(f"Course {in_string.upper()} by professor {names[in_string.upper()]} will start in room "
              f"{rooms[in_string.upper()]} at {times[in_string.upper()]}.")
    else:
        print(f"There's no data for course {in_string}.")


# Call the main function.
if __name__ == '__main__':
    main()
