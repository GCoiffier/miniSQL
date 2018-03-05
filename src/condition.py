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

    def __init__(self,attr,operator):
        Condition.__init__(self,operator)
        self.attr=attr

    def eval(self,entry):
        return True

class JoinCondition(Condition):

    def __init__(self, attr1, operator, attr2):
        Condition.__init__(self,operator)
        self.attrs = (attr1,attr2)

    def eval(self, entryA, entryB):
        if self.operator==Op.EQ:
            return True
        elif self.operator==Op.NEQ:
            return False
