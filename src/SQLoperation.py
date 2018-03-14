from database import *
from exceptions import *

## ________________ Projection _______________
def project(rel, attributes):
    indices = []
    for a in attributes :
        try:
            indices.append(rel._keys[a])
        except KeyError:
            raise Exception("key "+str(a) + " is not an attribute of relation "+ str(rel.get_keys()) )
    entries = [ tuple(line[i] for i in indices) for line in rel.data ]
    new = Relation("projectRequest", attributes, entries)
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
    filtered = []
    for x in rel.data:
        if verify_conditions(x, condList, rel._keys):
            filtered.append(x)
    return Relation("selectRequest", rel.get_keys(), filtered)

## ______________________ Join __________________________
def join(relA, relB, cond=None):
    """
    Cartesian product
    """
    entries = []
    for lineA in relA.data :
        for lineB in relB.data :
            new_line = tuple([i for i in lineA] + [i for i in lineB])
            entries.append(new_line)
    keysA = relA.get_keys()
    keysB = relB.get_keys()
    new = Relation("joinRequest", keysA+keysB, entries)
    return new

## _____________________ Union ___________________________
def union(relA,relB):
    entries = [line for line in relA.data] + [line for line in relB.data]
    new = Relation("unionRequest", relA.keys, entries)
    return new

## ________________________ Minus _____________________________
def minus(relA,relB):
    entries = [line for line in relA.data if not (line in relB.data)]
    new = Relation("minusRequest", relA.keys, entries)
    return new
