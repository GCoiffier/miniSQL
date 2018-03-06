import os

class Relation:

    def __init__(self, name, keys, entries):
        """
        name -> thename of the table. Filename should be <name>.csv

        keys -> list containing all attributes of the relation

        entries -> the list of entries of the table.
                    One entry is a tuple
        """
        self.name = name.split(".")[0] #getting rid of eventual .csv
        self.data = entries
        self.keys = keys

    def __getitem__(self, key):
        return self.data[key]

    def __repr__(self):
        # what to do when print(relation) is called
        output = ""
        for k in self.keys:
            output += str(k) + " | "
        output+="\n"
        for entry in self.data:
            for field in entry:
                output+= field + " | "
            output+="\n"
        return output


class DataBase:
    def __init__(self):
        self.tables = dict()

    def __getitem__(self, key):
        return self.tables[key]

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
        for t in self.tables.values():
            print(t)


DATAS = DataBase() # global variable containing every data
