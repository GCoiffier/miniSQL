## ___________ Debug output utility _______________
DEBUG=True

def print_debug(*args):
    global DEBUG
    if DEBUG:
        for what in args:
            print(what)

## ____________ Exception classes _________________
class EndOfExecution(Exception):
    pass

class InvalidCommand(Exception):
    pass

class UnknownTable(Exception):
    pass

class UnknownAttribute(Exception):
    pass

class VisitorError(Exception):
    pass
