import os
from os.path import join as pjoin
import csv

from request import Request
from database import Relation

class Parser:
    def __init__(self):
        return

    @staticmethod
    def read_data(filename):
        path = pjoin("data",filename)
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            entries = []
            for row in reader:
                entries.append(row)
        return Relation(filename, entries)

    @staticmethod
    def write_data(db):
        pass

    @staticmethod
    def read_request(req):
        return Request()
