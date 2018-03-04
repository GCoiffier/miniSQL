import parser
from database import datas

## ___________ Debug output utility _______________
DEBUG=True
def print_debug(what):
    global DEBUG
    if DEBUG: print(what)


## ____________ Exception classes _________________
class EndOfExecution(Exception):
    pass

class InvalidCommand(Exception):
    pass


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
            raise InvalidCommand()

        if mainKeyWord in [".end", ".quit", ".exit"]:
            raise EndOfExecution()

        elif mainKeyWord==".tables":
            datas.print_tables()

        if len(command)==1:
            raise InvalidCommand()

        # From now, every command has length >1

        elif mainKeyWord in [".open", ".read", ".load"]:
            dbName=command[1].split("/")[-1]
            assert_extension(dbName,"csv")
            newTable = parser.read_data(dbName)
            datas.add_table(newTable)

        elif mainKeyWord in [".unload", ".close"]:
            tableName=command[1]
            print(tableName)
            print_debug("unloading table " + tableName)
            datas.remove_table(tableName)

        elif mainKeyWord==".run":
            reqPath = command[1]
            reqName = reqPath.split("/")[-1]
            assert_extension(reqName,"sql")
            with open(reqPath) as req:
                reqString = " ".join(req.readlines())
                parser.run_request(reqString)


        else:
            parser.run_request(reqString)

    except InvalidCommand:
        print(inputString + " : Invalid Command")

    return
