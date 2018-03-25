from os.path import join as pjoin
import antlr4

from .miniSQLParser import miniSQLParser
from .miniSQLLexer import miniSQLLexer
from .visitor import Visitor

from database import *
from exceptions import *

def read_request(path):
    try:
        reqString=""
        path=pjoin("request",path)
        with open(path) as req:
            reqString = " ".join(req.readlines())
        return reqString
    except FileNotFoundError as e:
        print("Error in read_request : " + path + ", this file does not exist")

def run_request(reqString, outputPath=None):
    # 1/ Generate AST
    lexer = miniSQLLexer(antlr4.InputStream(reqString))
    stream = antlr4.CommonTokenStream(lexer)
    parser = miniSQLParser(stream)
    tree = parser.main() # rule 'main' is the entry point of the grammar

    # 2/ Run visitor
    visitor = Visitor()
    resultRelation = visitor.visit(tree)
    print_debug(" -- VISITING DONE --\n  Visitor exited without raising an error")

    # 3/ Output result
    if outputPath is None : # Output in terminal
        print(resultRelation)
    else :
        Table.to_file(resultRelation, outputPath)
