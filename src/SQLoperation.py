from database import *
from exceptions import *
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
def verify_conditions(entry, condList, keys):
    """
    condList is a list of list -> CDF form
    """
    for clause in condList: # OR
        clauseValue = True
        for cond in clause: # AND
            if not cond.eval(keys,entry):
                clauseValue=False
        if clauseValue:
            return True
    return False

def select(rel, condList):
    selection = lambda x : verify_conditions(x,condList, rel._keys)
    filtered = filter(selection , rel.data)
    return Table("selectRequest", rel.get_keys(), filtered)

## ______________________ Join __________________________
def join(relA, relB):
    """
    Cartesian product
    """
    if (isinstance(relA.data,Cursor) and isinstance(relB.data,Cursor)):
        def flatten(x):
            for a,b in x:
                yield a+b
        curA = relA.data
        curB = relB.data
        keysA = relA.get_keys()
        keysB = relB.get_keys()
        new = Table("joinRequest", keysA+keysB, flatten(product(curA,curB)))
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
    if (isinstance(relA.data,set) and isinstance(relB.data,set)):
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
