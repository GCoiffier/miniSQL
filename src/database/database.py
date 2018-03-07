import os
from exceptions import *
from .relation import Relation

class DataBase:
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
