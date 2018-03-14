import os
from exceptions import *
from .relation import Relation
from .attribute import Attribute
import parser

class DataManager:
    def __init__(self):
        self.tables = dict()

    def __getitem__(self, key):
        try:
            x = self.tables[key]
            return x
        except KeyError:
            raise UnknownTable("Table " + key + " is not present in the database !")

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

    def load(self,tableName):
        """
        Loads tables present in a request
        """
        if tableName not in self.tables.keys():
            rel = parser.read_data(tableName)
            self.add_table(rel)

    def rename_table(self,tableName,newTableName):
        rel = self.tables[tableName]
        newRel = Relation(newTableName, rel.get_keys(), rel.data)
        newRel.rename(newTableName)
        self.add_table(newRel)

    def get_tables(self,tableNames):
        return [self.tables[x] for x in tableNames]

    def print_tables(self):
        for t in self.tables.values():
            print(t)

    def discard(self):
        self.tables = dict()
