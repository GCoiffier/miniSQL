from commandLine import *
import parser
from SQLoperation import *
from database import *
from condition import *

rel = parser.read_data("test.csv")

"""
# Project test
rel2 = project(rel,["name","age"])
print(rel2)
"""

d = JoinCondition("age",Op.NEQ,"age")
d.eval(rel[0],rel[1])
