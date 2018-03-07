import os
from exceptions import *

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
