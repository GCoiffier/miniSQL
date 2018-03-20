from itertools import product
from cursor import *

def flatten(x):
    for a,b in x:
        yield a+b

x = Cursor("../../data/test.csv")
y = Cursor("../../data/employes.csv")
z = flatten(product(x,y))

for l in z:
    print(l)
