# function to find degree of number by using recursion

def main():
	# get number from user
	print("Please, enter a number for exponentiation: ")
	number = get_number(0)
	print("Please, enter degree, it should be > 0: ")
	degree = 0
	while degree <= 0:
		degree = get_number(1)
	print(f"{number} in degree {degree} is {count_degree(number, degree)}")


# type 0 to check for float, type 1 - int
def get_number(type):
	loop_flag = True
	while loop_flag:
		number = input("Enter a number: ")
		if type == 0:
			if is_float(number):
				number = float(number)
				loop_flag = False
		elif type == 1:
			if is_int(number):
				number = int(number)
				loop_flag = False
		else:
			print("Wrong type")
			number = None
			loop_flag = False
	return number

	
def count_degree(n, d):
	if d == 1:
		return n
	else:
		return n * count_degree(n, d - 1)


def is_int(number):
	try:
		int(number)
		return True
	except ValueError:
		return False


def is_float(number):
	try:
		float(number)
		return True
	except ValueError:
		return False


# Call the main function.
if __name__ == '__main__':
	main()
