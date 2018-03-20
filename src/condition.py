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
    def __init__(self, *args):
        assert len(args)>0
        self.args = args

    def __repr__(self):
        return "Or("+str(self.args)+")"

class And:
    def __init__(self, *args):
        assert len(args)>0
        self.args = args

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
        elif self.operator == Oq.NEQ:
            return entry1!=entry2
        elif self.operator == Oq.LT:
            return int(entry1)>=int(entry2)
        elif self.operator == Oq.LE:
            return int(entry1)>int(entry2)
        elif self.operator == Oq.GT:
            return int(entry1)<int(entry2)
        elif self.operator == Oq.GE:
            return int(entry1)<=int(entry2)

    def __repr__(self):
        return str((self.attr1, self.operator, self.attr2))

class BooleanCondition(Condition):
    def __init__(self,b):
        self.bool = b

    def eval(self,*args):
        return self.bool

    def __repr__(self):
        return "BooleanCondition("+str(self.bool)+")"

class InCondition(Condition):

    def __init__(self, attr, rel):
        self.rel = rel
        realName = self.rel.get_keys()[0]
        self.attr = Attribute(realName.table, attr.attr)

    def eval(self, keys, entry):
        entryAttr = entry[keys[self.attr]]
        for line in self.rel.data:
            if line[0]==entryAttr:
                return True
        return False

    def __repr__(self):
        return "InCondition("+str(self.attr)+","+ self.rel.name+")"


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
