from database import *
from exceptions import *
from condition import Or, And
from itertools import product,chain,dropwhile

## ________________ Projection _______________
def project(rel, attributes):
    indices = []
    for a in attributes :
        try:
            indices.append(rel.keys[a])
        except KeyError:
            raise UnknownAttribute("key "+str(a) + " is not an attribute of relation "+ str(rel.get_keys()) )
    projection = lambda x : tuple(x[i] for i in indices)
    entries = map(projection, rel.data)
    new = Table("projectRequest", attributes, entries)
    return new

## ______________ Selection __________________
def verify_conditions(entry, cond, keys):
    """
    condTree is a list of list -> CDF form
    """
    if isinstance(cond,Or):
        for clause in cond.args:
            if verify_conditions(entry,clause,keys):
                return True
        return False

    elif isinstance(cond,And):
        for clause in cond.args:
            if not verify_conditions(entry,clause,keys):
                return False
        return True

    else :
        return cond.eval(keys,entry)

def select(rel, condTree):
    selection = lambda x : verify_conditions(x, condTree, rel.keys)
    filtered = filter(selection , rel.data)
    new = Table("selectRequest", rel.get_keys(), filtered)
    return new

## ______________________ Join __________________________
def join(relA, relB):
    """
    Cartesian product
    """
    def flatten(x):
        for a,b in x:
            yield a+b
    keysA = relA.get_keys()
    keysB = relB.get_keys()
    new = Table("joinRequest", keysA+keysB, flatten(product(relA.data,relB.data)))
    return new

## _____________________ Union ___________________________
def union(relA,relB):
    entries = chain(relA.data,relB.data)
    new = Table("unionRequest", relA.get_keys(), entries)
    return new

## ________________________ Minus _____________________________
def minus(relA,relB):
    entries = dropwhile(lambda x : x in relB.data , relA.data)
    new = Table("minusRequest", relA.get_keys(), entries)
    return new
