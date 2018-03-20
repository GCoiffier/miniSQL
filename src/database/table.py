from os.path import join as pjoin
from itertools import tee

from exceptions import *
from .attribute import Attribute
from .cursor import Cursor

import csv

class Table:

    def __init__(self, name, keys, entries):
        """
        keys -> list containing all attributes of the relation
        entries -> the list of entries of the table.
                    One entry is a tuple
        """
        self.name = name
        self.data = entries
        self.keys = dict()
        if isinstance(keys[0],Attribute):
            for i,key in enumerate(keys):
                self.keys[key]=i
        else :
            for i,key in enumerate(keys):
                self.keys[Attribute(self.name,key)]=i

    def is_empty(self):
        return len(self.data)==0

    def rename(self,newName):
        """
        Rename table and all attributes into "table.attr" form
        """
        self.name = newName
        newKeys = dict()
        for key in self.keys:
            newKeyName = Attribute(newName,key.attr)
            newKeys[newKeyName]= self.keys[key]
        self.keys = newKeys

    def get_keys(self):
        """
        Return the list of keys in correct order
        """
        l = list(self.keys.keys())
        l = sorted(l, key= lambda x : int(self.keys[x]))
        return l

    def __repr__(self):
        output="\n"
        temp,self.data = tee(self.data)
        for entry in temp:
            for field in entry:
                output+= field + " | "
            output+="\n"
        return output

    @staticmethod
    def from_file(filename):
        """
        Builds a Relation object from a csv file.
        /!\ Assumes 'filename' has extension .csv
        """
        try:
            path = pjoin("data",filename)
            cursor = Cursor(path)
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                keys = reader.fieldnames
            print_debug("Loading table "+filename+" from file")
            return Table(filename, keys, cursor)
        except FileNotFoundError as e:
            print("Error in Relation.read_data : " + path + ", this file does not exist")
            return None
