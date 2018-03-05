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
    new = Relation("name",attributes,entries)
    return new

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

def join(relA,relB,cond=None):
    """
    Cartesian product
    """
    #TODO
    pass

def union(relA,relB):
    pass
