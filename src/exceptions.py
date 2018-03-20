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
