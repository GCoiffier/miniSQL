from commandLine import *
import parser
from SQLoperation import *
from database import *

rel = parser.read_data("test.csv")
rel2 = select(rel,["nom","age"])
print(rel2)
