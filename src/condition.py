from enum import Enum
from database import Attribute

from functools import reduce

class Op(Enum):
    """ Condition operator """
    EQ  = 1  # =
    NEQ = 2  # !=
    LT  = 3  # <
    LE  = 4  # <=
    GT  = 5  # >
    GE  = 6  # >=

def text_to_OP(txt):
    if txt == "=":
        return  Op.EQ
    elif txt == "!=":
        return  Op.NEQ
    elif txt == "<=":
        return  Op.LE
    elif txt == "<":
        return  Op.LT
    elif txt == ">=":
        return  Op.GE
    elif txt == ">":
        return  Op.GT

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
            return int(entry1)<int(entry2)
        elif self.operator == Op.LE:
            return int(entry1)<=int(entry2)
        elif self.operator == Op.GT:
            return int(entry1)>int(entry2)
        elif self.operator == Op.GE:
            return int(entry1)>=int(entry2)

    def __repr__(self):
        return str((self.attr1, self.operator, self.attr2))

class ConstCondition(Condition):
        def __init__(self, attr, operator, cst):
            self.attr=attr
            self.const=cst
            self.operator = operator

        def eval(self, keys, entry):
            e = entry[keys[self.attr]]
            if self.operator == Op.EQ:
                return e==self.const
            elif self.operator == Op.NEQ:
                return e!=self.const
            elif self.operator == Op.LT:
                return int(e)<int(self.const)
            elif self.operator == Op.LE:
                return int(e)<=int(self.const)
            elif self.operator == Op.GT:
                return int(e)>int(self.const)
            elif self.operator == Op.GE:
                return int(e)>=int(self.const)

        def __repr__(self):
            return str((self.attr, self.operator, self.const))

class NotInCond:
    def __init__(self, clauseIn):
        self.withIn = clauseIn

    def __repr__(self):
        return "NotInCond("+str(self.withIn)+")"

def toCNF(condTree):
    """
    Transforms a condition tree into a CNF formula
    """

    def CNFproduct(x,y):
        l = []
        for cx in x:
            for cy in y:
                l.append(And(cx,cy))
        return l

    if isinstance(condTree, Or):
        rec = [toCNF(x).args for x in condTree.args]
        return Or(reduce(rec,CNFproduct))
    elif isinstance(condTree, And):
        l = []
        for x in condTree.args :
            l.append(toCNF(x))
        l2=[]
        for x in l: # flatten all And
            l2 += x.args
        return Or(l2)
    else:
        return condTree
