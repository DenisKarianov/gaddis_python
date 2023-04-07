# Ackermann function to test recursion

def main():
	# get numbers from user
	print("Please, enter first number, it should be > 0: ")
	m = 0
	while m <= 0:  # loop to check that number is positive
		m = get_number(1)
	print("Please, enter second number, it should be > 0: ")
	n = 0
	while n <= 0:  # loop to check that number is positive
		n = get_number(1)

	print(ackermann(m, n))


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

	
def ackermann(m, n):
	if m == 0:
		return n + 1
	elif n == 0:
		return ackermann(m - 1, 1)
	else:
		return ackermann(m - 1, ackermann(m, n - 1))


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
