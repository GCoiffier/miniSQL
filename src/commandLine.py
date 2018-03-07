import parser
from exceptions import *
from database import *


## ___________ Command parser ______________________

COMMANDS = {".end", ".exit", ".quit", ".tables", ".open", ".read", ".load", ".run", ".close", ".unload"}

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
    .open path/to/table.csv  |  .read path/to/table.csv  | .load path/to/table.csv
    .close <table name> | .unload <table name>
    .tables
    .run path/to/request.sql
    <SQL request>
    """
    try:
        command = inputString.split()
        if len(command)==0: return

        # From now, every command has length >0
        mainKeyWord = command[0]

        if mainKeyWord[0]=="." and not (assert_command(mainKeyWord)):
            raise InvalidCommand("command '" + mainKeyWord + "' is invalid")

        if mainKeyWord in [".end", ".quit", ".exit"]:
            raise EndOfExecution()
            return

        elif mainKeyWord==".tables":
            DATAS.print_tables()
            return

        if len(command)==1:
            raise InvalidCommand("command '" + mainKeyWord + "' expected at least one argument")

        # From now, every command has length >1

        elif mainKeyWord in [".open", ".read", ".load"]:
            dbName=command[1]
            assert_extension(dbName,"csv")
            newTable = parser.read_data(dbName)
            if newTable is not None :
                DATAS.add_table(newTable)
            return

        elif mainKeyWord in [".unload", ".close"]:
            tableName=command[1]
            print(tableName)
            print_debug("unloading table " + tableName)
            DATAS.remove_table(tableName)
            return

        elif mainKeyWord==".run":
            reqPath = command[1]
            assert_extension(reqPath,"sql")
            reqString = parser.read_request(reqPath)
            if reqString is not None :
                parser.run_request(reqString)
            return

        else:
            parser.run_request(inputString)
            return

    except InvalidCommand as e :
        print(inputString + " : Invalid Command, "+ e.args[0])

    return
