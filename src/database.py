import os

class Relation:

    def __init__(self, name, entries):
        self.name = name.split(".")[0]
        self.data = entries
        assert(len(entries)>0)
        self.keys = entries[0].keys()

    def __repr__(self):
        # what to do when print(relation) is called
        output = "Table : " + self.name +"\n\n"
        for k in self.keys:
            output += str(k) + " | "
        output+="\n"
        for entry in self.data:
            for field in entry:
                output+=entry[field]+" | "
            output+="\n"
        return output
