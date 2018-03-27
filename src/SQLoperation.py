from database import *
from exceptions import *
from condition import Or, And, NotInCond
from itertools import product,chain,filterfalse,tee
from functools import reduce

## _____________________ Projection ____________________________________________
def project(rel, attributes):
    indices = []
    for a in attributes :
        try:
            indices.append(rel.keys[a])
        except KeyError:
            raise UnknownAttribute("key "+str(a) + " is not an attribute of relation "+ str(rel.get_keys()) )
    def projectionWithoutRepetition(iterable):
        mem = None
        for item in iterable:
            newEntry = tuple(item[i] for i in indices)
            if mem is None or mem != newEntry :
                mem = newEntry
                yield newEntry
    new = Table("projectRequest", attributes, projectionWithoutRepetition(rel.data))
    return new

## ____________________ Selection ______________________________________________
def verify_conditions(entry, cond, keys, ignoreNotIn):
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
    """
    Filters a table and keep only entries satisfying conditions in condTree
    """
    def is_not_previous(x,mem):
        if mem is None or x != mem :
            mem = x
            return True
        return False
    selection = lambda x : is_not_previous(x,None) and verify_conditions(x, condTree, rel.keys, ignoreNotIn)
    filtered = filter(selection , rel.data)
    new = Table("selectRequest", rel.get_keys(), filtered)
    return new

def select_distinct(rel):
    """
    Filters a table and delete duplicates
    """
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
    entries = filterfalse(lambda x : x in relB.get_data() , relA.data)
    new = Table("minusRequest", relA.get_keys(), entries)
    return new

## ________________________ Better Operators ___________________________________
def readSelectProjectRename(fileName, tableName, attr, isStar, conds):
    """
    Reads a CSV file, filter lines and transform remaning tuples
    keeping only the proper attributes after renaming
    """
    rel = Table.from_file(fileName)
    rel.rename(tableName)
    if conds is not None :
        rel = select(rel,conds)
    if not isStar :
        rel = project(rel,attr)
    return rel


def readSelectRenameGroupByProject(fileName, tableName, attr, isStar, conds, grpAttr, aggrOp):
    """
    Same as readSelectProjectRename but with a Group By Statement
    """
    rel = Table.from_file(fileName)
    rel.rename(tableName)
    if conds is not None :
        rel = select(rel,conds)
    rel = groupBy(rel, grpAttr, aggrOp)
    if not isStar :
        rel = project(rel,attr)
    return rel


def joinProjectRename(rel1,rel2, attr, conds):
    """
    Combines two relations in a θ-join and transform resulting tuples keeping
    only the proper attributes after renaming
    (the θ-join being a cartesian product followed by a selection)
    """
    rel = join(rel1,rel2)
    rel = select(rel,conds)
    rel = project(rel,attr)
    return rel

## _______________________ Aggregation and Group By ____________________________

def add_to_aggregate(aggr, entry, keyAggrOp):
    """
    Aggregates the entry 'entry' to entry aggr, using aggregation operators
    described in 'keyAggrOp' dict
    """
    if aggr is None :
        aggr = [None]*len(entry)
        for i in keyAggrOp.keys():
            if keyAggrOp[i]==Aggregation.COUNT:
                aggr[i]=1
            else:
                try:
                    aggr[i]=int(entry[i])
                except:
                    aggr[i]=entry[i]
    for i in keyAggrOp.keys():
        if keyAggrOp[i] == Aggregation.SUM:
            aggr[i] += int(entry[i])
        elif keyAggrOp[i] == Aggregation.MIN:
            aggr[i] = min(aggr[i], int(entry[i]))
        elif keyAggrOp[i] == Aggregation.MAX:
            aggr[i] = max(aggr[i], int(entry[i]))
        elif keyAggrOp[i] == Aggregation.COUNT:
            aggr[i] += 1
        elif keyAggrOp[i] == Aggregation.NONE:
            aggr[i]=entry[i]
    return aggr

def aggregate(rel, aggrOp):
    """
    Perform an aggregation on rel (all fields at once)
    """
    keyAggrOp = dict() # a dict int -> Aggregation operator
    for (attr,aggr) in aggrOp.items():
        keyAggrOp[rel.keys[attr]]=aggr
    data = [reduce(lambda x,y : add_to_aggregate(x,y, keyAggrOp), rel.get_data(), None)]
    rel = Table(rel.name, rel.get_keys(), iter(data))
    return rel

def groupBy(rel, grpAttr, aggrOp):
    """
    Perform a GROUP BY
    rel     : the initial table to aggregate
    grpAttr : the attribute 'GROUP BY grpAttr'
    aggrOp  : a dict  attribute->Aggregation operator
    """
    key = rel.keys[grpAttr]

    keyAggrOp = dict() # a dict int -> Aggregation operator
    for (attr,aggr) in aggrOp.items():
        keyAggrOp[rel.keys[attr]]=aggr

    datadict = dict()
    for entry in rel.get_data():
        try:
            value = int(entry[key])
        except:
            value = entry[key]
        if value not in datadict :
            datadict[value] = None
        datadict[value] = add_to_aggregate(datadict[value], entry , keyAggrOp)

    rel = Table("groupBy", rel.get_keys(), iter(datadict.values()) )
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
    sorted = [x for x in rel.get_data()]
    sorted.sort(key = compare, reverse=desc)
    return Table(rel.name, rel.get_keys(), iter(sorted))
