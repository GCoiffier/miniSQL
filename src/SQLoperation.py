from database import Relation

## ________________ Projection _______________
def project(rel,attributes):
    indices = []
    for key in attributes :
        i = 0
        while rel.keys[i] != key :
            print (rel.keys[i])
            print ("\n")
            print (key)
            print ("\n")
            i += 1
        indices.append(i)
    entries = []
    for line in rel.data :
        new_line = tuple(line[i] for i in indices)
        entries.append(new_line)
    new = Relation("SELECT_request",attributes,entries)
    return new


## ______________ Selection __________________
def verify_cond(entry,cond):
    #TODO
    return True

def verify_cond_list(entry,condList):
    for cond in condList:
        if not verify_cond(entry,cond):
            return False
    return True

def select(rel,condList):
    filtered = []
    for x in rel.datas:
        if verify_cond_list(x,condList):
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
    new = Relation("JOIN",relA.keys + relB.keys,entries)
    return new

## _____________________ Union ___________________________
def union(relA,relB):
    entries = [line for line in relA.data] + [line for line in relB.data]
    new = Releation("UNION",relA.keys,entries)
    return new
