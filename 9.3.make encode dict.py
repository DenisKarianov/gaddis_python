# program to make dictionary for encoding characters

import random
import pickle

RUS_ALPHA = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS = '''"' \n«».,?!:;—-=+()[]{}<>|/@#$%^&*_№…'''


def main():
    # make dict for encoding - key - text-symbol, value - encode-symbol
    symbol_file = open("symbols.txt", "r")
    symbol_str = symbol_file.read()
    symbol_file.close()
    # remove \n
    symbol_str = symbol_str.rstrip("\n")
    # make set from list to remove same symbols and after make a list to make later random.sample from it
    symbol_list = list(set(symbol_str))
    all_alpha = RUS_ALPHA + ENG_ALPHA + SYMBOLS  # make all characters for encoding to one string
    # make codes' list for all symbols
    encodes = random.sample(symbol_list, k=len(all_alpha))
    # make empty dict
    encode_dict = dict()
    for i, ch in enumerate(all_alpha):
        encode_dict[ch] = encodes[i]
    # conserve encode_dict to encodes.dat
    output_file = open('encodes.dat', 'wb')
    pickle.dump(encode_dict, output_file)
    output_file.close()
    print("Encode dictionary was saved successfully.")


# Call the main function.
if __name__ == '__main__':
    main()
