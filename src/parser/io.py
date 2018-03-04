import os
from os.path import join as pjoin
import csv

from database import Relation

def read_data(filename):
    """
    Builds a Relation object from a csv file.
    /!\ Assumes 'filename' has extension .csv
    """
    path = pjoin("data",filename)
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        keys = reader.fieldnames
        entries = []
        for row in reader:
            entries.append(list(row.values()))
    return Relation(filename, keys, entries)

def write_data(rel):
    pass

def run_request(reqString):
    # lex and parse
    lexer = MuLexer(antlr4.CharStream(reqString))
    stream = antlr4.CommonTokenStream(lexer)
    parser = MuParser(stream)
    tree = parser.prog()

    visitor = miniSQLVisitor()
    try:
        visitor.visit(tree)
    except:
        print("error in run_request")
