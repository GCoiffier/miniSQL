from database import *
from exceptions import *

## ________________ Projection _______________
def project(rel,attributes):
    indices = []
    output = "-- In projection :\n-- "
    for key in attributes :
        output += str(key) + " : " + str(rel.keys[key]) + " | "
        indices.append(rel.keys[key])
    print (output)
    print(rel)
    entries = [ tuple(line[i] for i in indices) for line in rel.data ]
    new = Relation("projectRequest",attributes,entries)
    return new


## ______________ Selection __________________
def verify_cond(entry,cond,keys):
    return FilterCondition(cond).eval(keys,entry)

def verify_cond_list(entry,condList,keys):
    for cond in condList:
        if not verify_cond(entry,cond,keys):
            return False
    return True

def select(rel,condList):
    filtered = []
    for x in rel.DATAS:
        if verify_cond_list(x,condList,rel.keys):
            filtered.append(x)
    return Relation("selectRequest",rel.keys,filtered)

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
    new = Relation("joinRequest",relA.keys + relB.keys, entries)
    return new

## _____________________ Union ___________________________
def union(relA,relB):
    entries = [line for line in relA.data] + [line for line in relB.data]
    new = Relation("unionRequest",relA.keys,entries)
    return new
