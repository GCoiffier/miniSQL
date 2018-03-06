from os.path import join as pjoin

import antlr4
import csv

from .miniSQLParser import miniSQLParser
from .miniSQLLexer import miniSQLLexer
from .visitor import miniSQLVisitor

from database import Relation
from debug import print_debug

def read_data(filename):
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
                entries.append(list(row.values()))
            return Relation(filename, keys, entries)
    except FileNotFoundError as e:
        print("Error in read_data : " + path + ", this file does not exist")
        return None

def write_data(rel):
    pass

def read_request(path):
    try:
        reqString=""
        path=pjoin("request",reqPath)
        with open(path) as req:
            reqString = " ".join(req.readlines())
        return reqString
    except FileNotFoundError as e:
        print("Error in read_request : " + path + ", this file does not exist")

def run_request(reqString):
    # lex and parse
    lexer = miniSQLLexer(antlr4.InputStream(reqString))
    stream = antlr4.CommonTokenStream(lexer)
    parser = miniSQLParser(stream)
    tree = parser.main() # rule 'main' is the entry point of the grammar

    # visit and execute request
    visitor = miniSQLVisitor()
    resultRelation = visitor.visit(tree)
    print_debug("Visiting exited without raising an error")
    print(resultRelation)
