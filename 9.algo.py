# instruction to save dictionary in file and load saved object from file

import pickle

test_averages = {'Janel': 98, 'Thomas': 74, 'Sam': 87, 'Sally': 89, 'Jennifer': 92, 'Zeb': 84}

# save to file
outfile = open('mydata.dat', 'wb')
pickle.dump(test_averages, outfile)
outfile.close()

# load from file
infile = open('mydata.dat', 'rb')
dct = pickle.load(infile)
print(dct)
