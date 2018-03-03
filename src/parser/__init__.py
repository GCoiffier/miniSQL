import antlr4
import sys
from subprocess import call

from .parser import *

try:
    from .miniSQLLexer import miniSQLLexer
    from .miniSQLParser import miniSQLParser
except:
    print("Antlr lexer/parser has not been found")
