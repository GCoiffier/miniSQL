from enum import Enum

class Attribute:

    def __init__(self, table, attr):
        self.table = table
        self.attr = attr
        self.fullName = table+"."+attr

    def __hash__(self):
        return hash((self.table, self.attr))

    def __eq__(self, other):
        return (self.table, self.attr) == (other.table, other.attr)

    def __repr__(self):
        return "Attribute("+self.table+","+self.attr+")"

    def __str__(self):
        return self.attr

class Aggregation(Enum):
    """ Aggregation operator """
    SUM     = 1  # +
    MIN     = 2  # min
    MAX     = 3  # max
    COUNT   = 4
    AVG     = 5  # average
    GROUPBY = 6  # No function as it is the attribute we group by
