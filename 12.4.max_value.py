# function to find max value in list by using recursion

def main():
	# make some list with numbers
	num_list = [1, 34, 9993, 2, 55, 66, 3, 777, 333, 33, 466, 3300]
	max_val = get_max(num_list)
	print(max_val)


def get_max(inlist):
	if len(inlist) == 1:
		return inlist[0]
	else:
		if inlist[0] >= inlist[1]:
			inlist.remove(inlist[1])  # remove number, than less or even
			return get_max(inlist)
		else:
			inlist.remove(inlist[0])
			return get_max(inlist)


# Call the main function.
if __name__ == '__main__':
	main()
