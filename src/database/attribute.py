class Attribute:
    def __init__(self,table,attr):
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
