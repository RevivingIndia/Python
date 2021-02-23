#dums() and loads() method

import pickle

my_list = [1,2,3,4]

x = pickle.dumps(my_list)
print('pickling objet',x)

y = pickle.loads(x)
print('unpickling object',y)
