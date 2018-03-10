import os
from exceptions import *

class Attribute:
    def __init__(self,table,attr):
        self.table = table
        self.attr = attr
        self.fullName = table+"."+attr

    def __repr__(self):
        return "Attribute("+self.table+","+self.attr+")"

    def __str__(self):
        return self.attr

class Relation:

    def __init__(self, name, keys, entries):
        """
        name -> thename of the table. Filename should be <name>.csv

        keys -> list containing all attributes of the relation

        entries -> the list of entries of the table.
                    One entry is a tuple
        """
        self.name = name
        self.data = entries
        self.keys = dict()
        for i,key in enumerate(keys):
            self.keys[key]=i

    def __getitem__(self, index):
        return self.data[index]

    def get_keys(self):
        l = list(self.keys.keys())
        l = sorted(l, key= lambda x : int(self.keys[x])
        return l

    def __repr__(self):
        """ what to do when print(relation) is called
        """
        output = ""

        for k in self.get_keys():
            output += str(k) + " | "
        output+="\n"

        for entry in self.data:
            for field in entry:
                output+= field + " | "
            output+="\n"
        return output
