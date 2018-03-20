from database import *
from exceptions import *
from condition import Or, And

## ________________ Projection _______________
def project(rel, attributes):
    indices = []
    for a in attributes :
        try:
            indices.append(rel._keys[a])
        except KeyError:
            raise UnknownAttribute("key "+str(a) + " is not an attribute of relation "+ str(rel.get_keys()) )
    projection = lambda x : tuple(x[i] for i in indices)
    entries = set(map(projection, rel.data))
    new = Table("projectRequest", attributes, entries)
    return new


## ______________ Selection __________________
def verify_conditions(entry, cond, keys):
    """
    condList is a list of list -> CDF form
    """
    print(cond)
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

def select(rel, condList):
    filtered = filter(lambda x : verify_conditions(x,condList, rel._keys) , rel.data)
    return Table("selectRequest", rel.get_keys(), filtered)

## ______________________ Join __________________________
def join(relA, relB, cond=None):
    """
    Cartesian product
    """
    entries = set()
    for lineA in relA.data :
        for lineB in relB.data :
            new_line = tuple([i for i in lineA] + [i for i in lineB])
            entries.add(new_line)
    keysA = relA.get_keys()
    keysB = relB.get_keys()
    new = Table("joinRequest", keysA+keysB, entries)
    return new

## _____________________ Union ___________________________
def union(relA,relB):
    entries = relA.data.union(relB.data)
    new = Table("unionRequest", relA.keys, entries)
    return new

## ________________________ Minus _____________________________
def minus(relA,relB):
    entries = relA.data - relB.data
    new = Table("minusRequest", relA.keys, entries)
    return new
