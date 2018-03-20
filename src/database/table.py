from os.path import join as pjoin

from exceptions import *
from .attribute import Attribute

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
        self._keys = dict()
        if isinstance(keys[0],Attribute):
            for i,key in enumerate(keys):
                self._keys[key]=i
        else :
            for i,key in enumerate(keys):
                self._keys[Attribute(self.name,key)]=i

    def is_empty(self):
        return len(self.data)==0

    def rename(self,newName):
        """
        Rename table and all attributes into "table.attr" form
        """
        self.name = newName
        newKeys = dict()
        for key in self._keys:
            newKeyName = Attribute(newName,key.attr)
            newKeys[newKeyName]= self._keys[key]
        self._keys = newKeys

    def get_keys(self):
        """
        Return the list of keys in correct order
        """
        l = list(self._keys.keys())
        l = sorted(l, key= lambda x : int(self._keys[x]))
        return l

    def __repr__(self):
        output = "\n"
        """
        for k in self.get_keys():
            output += str(k) + " | "
        output+="\n"
        """
        for entry in self.data:
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
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                keys = reader.fieldnames
                entries = []
                for row in reader:
                    newEntry=[]
                    for key in keys:
                        newEntry.append(row[key])
                    entries.append(tuple(newEntry))
                return Table(filename, keys, entries)
        except FileNotFoundError as e:
            print("Error in Relation.read_data : " + path + ", this file does not exist")
            return None