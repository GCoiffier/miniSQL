import os

class Relation:

    def __init__(self, name, entries):
        """
        name -> thename of the table. Filename should be <name>.csv
        entries -> the list of entries of the table.
                    One entry if a dictionnary field |-> value
        """
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
        """
        Loads a new table 'rel' into the database
        """
        self.tables[rel.name] = rel

    def remove_table(self,relName):
        """
        Removes table of name 'relName' from database
        """
        del self.tables[relName]

    def save(self):
        """
        Save all tables into their csv files
        """
        #TODO
        pass

    def discard(self):
        """
        Delete all tables (not files)
        """
        self.tables=dict()

    def print_tables(self):
        for t in self.tables.items():
            print(t[1])


datas = DataBase() # global variable containing every data
