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

class DataBase:
    def __init__(self):
        self.tables = dict()

    def add_table(self,rel):
        self.tables[rel.name] = rel

    def remove_table(self,relName):
        del self.tables[relName]

    def save(self):
        pass

    def discard(self):
        self.tables=dict()

    def print_tables(self):
        for t in self.tables.items():
            print(t[1])


datas = DataBase() # global variable containing every data
