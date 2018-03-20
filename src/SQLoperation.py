from database import *
from exceptions import *
from condition import Or, And
from itertools import product,chain

## ________________ Projection _______________
def project(rel, attributes):
    indices = []
    for a in attributes :
        try:
            indices.append(rel._keys[a])
        except KeyError:
            raise UnknownAttribute("key "+str(a) + " is not an attribute of relation "+ str(rel.get_keys()) )
    projection = lambda x : tuple(x[i] for i in indices)
    entries = map(projection, rel.data)
    if (isinstance(rel.data, list)):
        entries = list(entries)
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
    selection = lambda x : verify_conditions(x, condTree, rel._keys)
    filtered = filter(selection , rel.data)
    new = Table("selectRequest", rel.get_keys(), filtered)
    return new

## ______________________ Join __________________________
def join(relA, relB):
    """
    Cartesian product
    """
    if (not isinstance(relA.data,list) and not isinstance(relB.data,list)):
        def flatten(x):
            for a,b in x:
                yield a+b
        keysA = relA.get_keys()
        keysB = relB.get_keys()
        new = Table("joinRequest", keysA+keysB, flatten(product(relA.data,relB.data)))
        return new
    else :
        entries = []
        for lineA in relA.data :
            for lineB in relB.data :
                new_line = lineA + lineB
                entries.append(new_line)
        keysA = relA.get_keys()
        keysB = relB.get_keys()
        new = Table("joinRequest", keysA+keysB, entries)
        return new

## _____________________ Union ___________________________
def union(relA,relB):
    if (isinstance(relA.data,list) and isinstance(relB.data,list)):
        entries = relA.data + relB.data
    elif (isinstance(relA.data, Cursor) and isinstance(relB.data, Cursor)):
        entries = chain(relA.data,relB.data)
    else:
        if (isinstance(relA.data,Cursor)):
            relA,relB=relB,relA
        entries = relA.data
        for x in relB.data:
            entries.append(x)
    new = Table("unionRequest", relA.keys, entries)
    return new

## ________________________ Minus _____________________________
def minus(relA,relB):
    entries = [x for x in relA if x not in relB]
    new = Table("minusRequest", relA.keys, entries)
    return new
