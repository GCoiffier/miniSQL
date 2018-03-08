from enum import Enum

class Op(Enum):
    """ Condition operator """
    EQ  = 1  # =
    NEQ = 2  # !=
    LT  = 3  # <
    LE  = 4  # <=
    GT  = 5  # >
    GE  = 6  # >=

class Condition:

    def __init__(self,operator):
        assert(isinstance(operator,Op))
        self.operator = operator

class FilterCondition(Condition):

    def __init__(self, attr1, operator, attr2):
        Condition.__init__(self,operator)
        self.attr1=attr1
        self.attr2=attr2
        self.attr2=value

    def eval(self, keys, entry):
        index = -1
        for key in keys :
            if key==self.attr:
                break
            i+=1
        if self.operator == Op.EQ:
            return self.attr2==entry[key]
        elif self.operator == Oq.NEQ:
            return self.attr2!=entry[key]
        elif self.operator == Oq.LT:
            return int(self.attr2)>=int(entry[key])
        elif self.operator == Oq.LE:
            return int(self.attr2)>int(entry[key])
        elif self.operator == Oq.GT:
            return int(self.attr2)<int(entry[key])
        elif self.operator == Oq.GE:
            return int(self.attr2)<=int(entry[key])

class JoinCondition(Condition):

    def __init__(self, attr, operator):
        Condition.__init__(self,operator)
        self.attr = attr

    def eval(self, entryA, entryB):
        if self.operator==Op.EQ:
            return True
        elif self.operator==Op.NEQ:
            return False
        elif self.operator == Oq.LT:
            return True
        elif self.operator == Oq.LE:
            return True
        elif self.operator == Oq.GT:
            return True
        elif self.operator == Oq.GE:
            return True
