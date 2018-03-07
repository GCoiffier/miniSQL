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

class UnknownTable(Exception):
    pass
