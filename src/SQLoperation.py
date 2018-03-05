from database import Relation

def select(rel,attributes):
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

def join(relA,relB,cond=None):
    entries = []
    for lineA in relA.data :
        for lineB in relB.data :
            new_line = tuple([i for i in lineA] + [i for i in lineB])
            entries.append(new_line)
    new = Relation("JOIN",relA.keys + relB.keys,entries)
    return new
        

def union(relA,relB):
    entries = [line for line in relA.data] + [line for line in relB.data]
    new = Releation("UNION",relA.keys,entries)
    return new
