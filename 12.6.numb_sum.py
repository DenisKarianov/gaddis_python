# function to find sum of integer numbers that contains in some number
# for expample for 5 it will be sum of 1, 2, 3, 4 and 5

def main():
	# get number from user
	# validation loop
	loop_flag = True
	while loop_flag:
		number = input("Enter integer number to get its sum: ")
		if is_int(number):
			number = int(number)
			loop_flag = False
	print(get_sum(number))


def get_sum(n):
	if n == 1:
		return n
	else:
		return n + get_sum(n - 1)


def is_int(number):
	try:
		int(number)
		return True
	except ValueError:
		return False


# Call the main function.
if __name__ == '__main__':
	main()
