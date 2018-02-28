################################################################################
#                        Data Base & Data Mining
#                              ENS de Lyon
#                              Spring 2018
#
#                           Project : MiniSQL
#
#                           Guillaume Coiffier
################################################################################

from parser import Parser

def main():
    rel = Parser.read_data("test.csv")
    print(rel)
    
if __name__=="__main__":
    main()
