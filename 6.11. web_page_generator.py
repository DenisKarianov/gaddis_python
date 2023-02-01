# program that generate web page about user.

# global constants
FILE_NAME = 'index.html'

def main():
    output_file = open(FILE_NAME, 'w')  # open a file for writing
    name = input("Enter your name: ")
    descr = input("Tell about yourself: ")
    output_file.write('<html>' + '\n')
    output_file.write('<head>' + '\n')
    output_file.write('</head>' + '\n')
    output_file.write('<body>' + '\n')
    output_file.write('    <center>' + '\n')
    output_file.write('    <h1>' + name + '</h1>' + '\n')
    output_file.write('    </center>' + '\n')
    output_file.write('    <hr />' + '\n')
    output_file.write('    ' + descr + '\n')
    output_file.write('    <hr />' + '\n')
    output_file.write('</body>' + '\n')
    output_file.write('</html>' + '\n')
    output_file.close()


main()
