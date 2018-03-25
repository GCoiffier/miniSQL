from database import *
from exceptions import *
from condition import Or, And, NotInCond
from itertools import product,chain,dropwhile,tee

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

## ____________________ Selection ______________________________________________
def verify_conditions(entry, cond, keys, ignoreNotIn):
    """
    condTree is a list of list -> CDF form
    """
    if isinstance(cond,Or):
        for clause in cond.args:
            if verify_conditions(entry,clause,keys,ignoreNotIn):
                return True
        return False

    elif isinstance(cond,And):
        for clause in cond.args:
            if not verify_conditions(entry,clause,keys,ignoreNotIn):
                return False
        return True

    elif isinstance(cond,NotInCond):
        if ignoreNotIn :
            return True
        else :
            cond = And(cond.withIn)
            return verify_conditions(entry,cond,keys,ignoreNotIn)

    else :
        return cond.eval(keys,entry)

def select(rel, condTree, ignoreNotIn=True):
    selection = lambda x : verify_conditions(x, condTree, rel.keys, ignoreNotIn)
    filtered = filter(selection , rel.data)
    new = Table("selectRequest", rel.get_keys(), filtered)
    return new

def select_distinct(rel):
    def unique_values(iterable):
        seen = set()
        for item in iterable:
            if tuple(item) not in seen:
                seen.add(tuple(item))
                yield item
    return Table("distinctProject", rel.get_keys(), unique_values(rel.data))

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

def add_to_aggregate(aggr, entry, keyAggrOp):
    if aggr is None :
        aggr = [None]*len(entry)
    for i in keyAggrOp.keys():
        if keyAggrOp[i] == Aggregation.SUM:
            if aggr[i] is None :
                aggr[i] = int(entry[i])
            else:
                aggr[i] += int(entry[i])
        elif keyAggrOp[i] == Aggregation.MIN:
            if aggr[i] is None :
                aggr[i] = int(entry[i])
            else:
                aggr[i] = min(aggr[i], int(entry[i]))
        elif keyAggrOp[i] == Aggregation.MAX:
            if aggr[i] is None :
                aggr[i] = int(entry[i])
            else:
                aggr[i] = max(aggr[i], int(entry[i]))
        elif keyAggrOp[i] == Aggregation.COUNT:
            if aggr[i] is None :
                aggr[i] = 1
            else:
                aggr[i] += 1
        elif keyAggrOp[i] == Aggregation.NONE:
            aggr[i]=entry[i]
    return aggr

def groupBy(rel, grpAttr, aggrOp):
    """
    Perform a GROUP BY
    rel     : the initial table to aggregate
    grpAttr : the attribute 'GROUP BY grpAttr'
    aggrOp  : a dict  attribute->Aggregation operator
    """
    key = rel.keys[grpAttr]
    print_debug("## ", grpAttr, key)

    keyAggrOp = dict() # a dict int -> Aggregation operator
    for (attr,aggr) in aggrOp.items():
        keyAggrOp[rel.keys[attr]]=aggr
    keyAggrOp[key]=Aggregation.NONE

    print(keyAggrOp)

    datadict = dict()
    for entry in rel.get_data():
        try:
            value = int(entry[key])
        except:
            value = entry[key]
        if value not in datadict :
            datadict[value] = None
        datadict[value] = add_to_aggregate(datadict[value], entry , keyAggrOp)
    rel = Table("groupBy", list(aggrOp.keys()), iter(datadict.values()) )
    rel = project(rel, list(aggrOp.keys()))
    return rel


## __________________________ Order By ____________________________

def orderBy(rel, attr, desc=False):
    """
    Order the entries of table rel according to attr.
    """

    def compKeys(x):
        l = []
        for a in attr:
            try:
                v = int(x[rel.keys[a]])
            except:
                v= x[rel.keys[a]]
            l.append(v)
        return l

    compare = lambda x : compKeys(x)
    sorted = [x for x in rel.data]
    sorted.sort(key = compare, reverse=desc)
    return Table(rel.name, rel.get_keys(), iter(sorted))
