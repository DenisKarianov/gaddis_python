# function to print stars in n lines from 1 star in first line to n star in last line

def main():
	n = 10
	star(n)


def star(n):
	if n > 1:
		star(n - 1)
	for s in range(n):
		print('*', end='')
	print()


# Call the main function.
if __name__ == '__main__':
	main()
