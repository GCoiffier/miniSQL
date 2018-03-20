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

def run_request(reqString):
    lexer = miniSQLLexer(antlr4.InputStream(reqString))
    stream = antlr4.CommonTokenStream(lexer)
    parser = miniSQLParser(stream)
    tree = parser.main() # rule 'main' is the entry point of the grammar
    #try:
    visitor = Visitor()
    resultRelation = visitor.visit(tree) # run visitor
    print_debug("Visiting exited without raising an error")
    print(resultRelation)
    #except Exception as e :
    #    print ("[ERROR] " + e.args[0])
