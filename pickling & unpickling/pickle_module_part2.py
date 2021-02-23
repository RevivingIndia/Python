#dum() and load() method

import pickle

my_list = [1,2,3,4]

with open('test.txt','wb') as f:
    pickle.dump(my_list,f)


#unpickling

x = open('test.txt','rb')
result = pickle.load(x)
print(x)
