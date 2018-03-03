import os
from os.path import join as pjoin
import csv

from request import Request
from database import Relation

def read_data(filename):
    path = pjoin("data",filename)
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        entries = []
        for row in reader:
            entries.append(row)
    return Relation(filename, entries)

def write_data(db):
    pass

def read_request(req):
    return Request()
