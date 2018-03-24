from enum import Enum
from database import Attribute

class Op(Enum):
    """ Condition operator """
    EQ  = 1  # =
    NEQ = 2  # !=
    LT  = 3  # <
    LE  = 4  # <=
    GT  = 5  # >
    GE  = 6  # >=

class Or:
    def __init__(self, clauseList):
        self.args = clauseList

    def __repr__(self):
        return "Or("+str(self.args)+")"

class And:
    def __init__(self, clauseList):
        self.args = clauseList

    def __repr__(self):
        return "And("+str(self.args)+")"

class Condition:

    def __init__(self, attr1, operator, attr2):
        self.attr1=attr1
        self.attr2=attr2
        self.operator = operator

    def eval(self, keys, entry):
        entry1 = entry[keys[self.attr1]]
        entry2 = entry[keys[self.attr2]]
        if self.operator == Op.EQ:
            return entry1==entry2
        elif self.operator == Op.NEQ:
            return entry1!=entry2
        elif self.operator == Op.LT:
            return int(entry1)>=int(entry2)
        elif self.operator == Op.LE:
            return int(entry1)>int(entry2)
        elif self.operator == Op.GT:
            return int(entry1)<int(entry2)
        elif self.operator == Op.GE:
            return int(entry1)<=int(entry2)

    def __repr__(self):
        return str((self.attr1, self.operator, self.attr2))

def tseitin(condTree):
    """
    Tseitin transformation, from :
        https://en.wikipedia.org/wiki/Tseytin_transformation
    Converts an arbitrary boolean formula into a CNF
    Useful in MINUS and NOT IN requests.
    """
    return None

class NotInCondition(Condition):

    def __init__(self, attr, rel):
        self.rel = rel
        realName = self.rel.get_keys()[0]
        self.attr = Attribute(realName.table, attr.attr)

    def eval(self, keys, entry):
        entryAttr = entry[keys[self.attr]]
        for line in self.rel.data:
            if line[0]==entryAttr:
                return False
        return True

    def __repr__(self):
        return "NotInCondition("+str(self.attr)+","+ self.rel.name+")"
