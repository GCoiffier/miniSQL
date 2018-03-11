import os
from exceptions import *
from .attribute import Attribute

class Relation:

    def __init__(self, name, keys, entries):
        """
        name -> the name of the table. Filename should be <name>.csv
        keys -> list containing all attributes of the relation
        entries -> the list of entries of the table.
                    One entry is a tuple
        """
        self.name = name
        self.data = entries
        self._keys = dict()
        typecheck = isinstance(keys[0],Attribute)
        if typecheck:
            for i,key in enumerate(keys):
                self._keys[key]=i
        else :
            for i,key in enumerate(keys):
                self._keys[Attribute("",key)]=i

    def belongs(self,entry):
        for e in self.data:
            if entry==e:
                return True
        return False

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

    def __getitem__(self, index):
        return self.data[index]

    def get_keys(self):
        """
        Return the list of keys in correct order
        """
        l = list(self._keys.keys())
        l = sorted(l, key= lambda x : int(self._keys[x]))
        return l

    def __repr__(self):
        output = ""

        for k in self.get_keys():
            output += str(k) + " | "
        output+="\n"

        for entry in self.data:
            for field in entry:
                output+= field + " | "
            output+="\n"
        return output
