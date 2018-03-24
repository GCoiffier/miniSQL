from database import *
from exceptions import *
from condition import Or, And
from itertools import product,chain,dropwhile

## _____________________ Projection ____________________________________________
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

def project_distinct(rel):
    def unique_values(iterable):
        seen = set()
        for item in iterable:
            if item not in seen:
                seen.add(item)
                yield item
    return Table("distinctProject", rel.get_keys(), unique_values(rel.data))

## ____________________ Selection ______________________________________________
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

## ______________________ Join _________________________________________________
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

## _______________________ Union _______________________________________________
def union(relA,relB):
    entries = chain(relA.data,relB.data)
    new = Table("unionRequest", relA.get_keys(), entries)
    return new

## ___________________________ Minus ___________________________________________
def minus(relA,relB):
    entries = dropwhile(lambda x : x in relB.data , relA.data)
    new = Table("minusRequest", relA.get_keys(), entries)
    return new


## ________________________ Better Operators ___________________________________

def readSelectProjectRename(filename, tableName, attr, conds,):
    """
    Reads a CSV file, filter lines and transform remaning tuples
    keeping only the proper attributes after renaming
    """
    rel = Table.from_file(filename)
    rel = rel.rename(tableName)
    rel = select(rel,conds)
    rel = project(rel,attr)
    return rel

def joinProjectRename(rel1,rel2, attr, conds):
    """
    Combines two relations in a θ-join and transform resulting tuples keeping
    only the proper attributes after renaming
    (the θ-join being a cartesian product followed by a selection)
    """

    pass

## __________________________ Group By ____________________________

def groupBySingleRelation(rel,attr):
    return rel

## __________________________ Order By ____________________________

def orderBy(rel, attr, desc=False):
    """
    Order the entries of table rel according to attr.
    """
    compare = lambda x : [int(x[rel.keys[a]]) for a in attr]
    sorted = [x for x in rel.data]
    sorted.sort(key = compare, reverse=desc)
    return Table(rel.name, rel.get_keys(), iter(sorted))
