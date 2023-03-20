# program to encode txt-file

import pickle

SAVEFILE = 'encoded_text.txt'
TEXTFILE = 'peresolil.txt'
ENCODESFILE = 'encodes.dat'


def main():
    # open file to encode
    try:
        infile = open(TEXTFILE, "r")
        txt_str = infile.read()
        infile.close()
        txt_str = txt_str.rstrip("\n")
        # load encode_dict from encodes.dat
        try:
            dict_file = open(ENCODESFILE, 'rb')
            try:
                encodes_dict = pickle.load(dict_file)
                dict_file.close()
                # encode txt data
                encoded_str = ''  # make empty string to save encoded data
                for ch in txt_str:
                    encoded_str += encodes_dict[ch]
                # save encoded string to txt-file
                outfile = open(SAVEFILE, 'w')
                outfile.write(encoded_str)
                outfile.close()
            except EOFError:
                print("Cannot load encode dictionary.")
        except FileNotFoundError:
            print("Cannot open encode dictionary file.")
    except FileNotFoundError:
        print(f"File {TEXTFILE} is not found.")


# Call the main function.
if __name__ == '__main__':
    main()
