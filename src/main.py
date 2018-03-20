################################################################################
#                        Data Base & Data Mining                               #
#                              ENS de Lyon                                     #
#                              Spring 2018                                     #
#                                                                              #
#                           Project : MiniSQL                                  #
#                                                                              #
#                           Guillaume Coiffier                                 #
#                            Nicolas Champseix                                 #
################################################################################

import sys
import os
import atexit
import readline

import parser
from exceptions import *
from database import *

## ________________ Command reader _________________________________________
COMMANDS = [".end", ".exit", ".quit", ".run", ".read"]

def assert_command(keyWord):
    """ Checks if we are given a supported command"""
    print_debug("asserting "+keyWord+" is a correct command")
    return (keyWord in COMMANDS)

def assert_extension(path,ext):
    """ Checks the extension of a given file"""
    print_debug("asserting " + path + " has extension " + ext)
    ext_path = path.split(".")[-1]
    return ext==ext_path

def run_command(inputString):
    """
    miniSQL commands :

    .exit | .quit | .end

    .run |.read path/to/request.sql

    <SQL request>
    """
    try:
        command = inputString.split()
        if len(command)==0:
            return
        # From now, every command has length >0

        mainKeyWord = command[0]

        if mainKeyWord[0]=="." and not (assert_command(mainKeyWord)):
            raise InvalidCommand("command '" + mainKeyWord + "' is invalid")

        if mainKeyWord in [".end", ".quit", ".exit"]:
            raise EndOfExecution()

        if len(command)==1:
            raise InvalidCommand("command '" + mainKeyWord + "' expected at least one argument")
        # From now, every command has length >1

        if mainKeyWord in [".run", ".read"]:
            reqPath = command[1]
            assert_extension(reqPath,"sql")
            reqString = parser.read_request(reqPath)
            if reqString is not None :
                parser.run_request(reqString)

        else:
            parser.run_request(inputString)

    except InvalidCommand as e :
        print(inputString + " : Invalid Command, "+ e.args[0])

## _______________ Auto completion and history in command line _________________

requestFiles = [req for _,_,req in os.walk("request")][0]
TO_COMPLETE = COMMANDS + requestFiles

def completer(text, state):
    options = [i for i in TO_COMPLETE if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

## _______________________ MAIN ________________________________________________
def main():
    try:
        while True:
            inputString = input("> ")
            run_command(inputString)
    except EndOfExecution:
        print("Program terminating !")
        return
    except EOFError:
        print("")
        return


if __name__=="__main__":
    histfile = os.path.join(os.path.expanduser(os.getcwd()), ".command_history")
    try:
        readline.read_history_file(histfile)
        readline.set_history_length(100)
    except FileNotFoundError:
        pass

    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    main()
    atexit.register(readline.write_history_file, histfile)
