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

    def __init__(self, attr, operator, val):
        pass
