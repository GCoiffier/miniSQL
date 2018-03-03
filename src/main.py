################################################################################
#                        Data Base & Data Mining
#                              ENS de Lyon
#                              Spring 2018
#
#                           Project : MiniSQL
#
#                           Guillaume Coiffier
################################################################################

from commandLine import run_command, EndOfExecution
import sys

def main():
    try:
        while True:
            sys.stdout.write('>')
            inputString = input()
            run_command(inputString)
    except EndOfExecution:
        print("Program terminating !")
        return


if __name__=="__main__":
    main()
