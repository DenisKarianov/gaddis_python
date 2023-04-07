# function to find sum of numbers in list by using recursion

def main():
	# make some list with numbers
	num_list = [1, 34, 9993, 2, 55, 66, 3, 777, 333, 33, 466, 3300]
	print(get_sum(num_list))


def get_sum(inlist):
	l = len(inlist)
	if len(inlist) == 1:
		return inlist[0]
	else:
		return inlist[l - 1] + get_sum(inlist[:l - 1])


# Call the main function.
if __name__ == '__main__':
	main()
