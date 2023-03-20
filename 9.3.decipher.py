# program to decipher txt-file

import pickle

OPENFILE = 'encoded_text.txt'
ENCODESFILE = 'encodes.dat'


def main():
    # open file to decipher
    try:
        infile = open(OPENFILE, "r")
        txt_str = infile.read()
        infile.close()
        txt_str = txt_str.rstrip("\n")
        # load encode_dict from encodes.dat
        try:
            dict_file = open(ENCODESFILE, 'rb')
            try:
                encodes_dict = pickle.load(dict_file)
                dict_file.close()
                # decipher txt data
                decoded_str = ''  # make empty string to save decoded data
                for ch in txt_str:
                    decoded_str += get_key(encodes_dict, ch)
                # print decoded string
                print(decoded_str)
                # save decoded string to txt-file
                outputfile = open('decoded.txt', 'w')
                outputfile.write(decoded_str)
                outputfile.close()
            except EOFError:
                print("Cannot load encode dictionary.")
        except FileNotFoundError:
            print("Cannot open encode dictionary file.")
    except FileNotFoundError:
        print(f"File {OPENFILE} is not found.")


def get_key(d, v):
    for key, value in d.items():
        if v == value:
            return key


# Call the main function.
if __name__ == '__main__':
    main()
