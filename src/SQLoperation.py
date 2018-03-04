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
    new = Relation("name",attributes,entries)
    return new

def join(relA,relB,cond=None):
    pass

def union(relA,relB):
    pass
