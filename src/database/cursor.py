import csv

class Cursor:

    def __init__(self,_filename):
        self.filename = _filename
        self.file = open(_filename,'r')
        self.file.readline() #get rid of headers
        self.reader = csv.reader(self.file)

    def __iter__(self):
        return self.reader.__iter__()

    def __next__(self):
        try:
            x = next(self.reader)
            return x
        except StopIteration:
            return None

    def reset(self):
        self.file.close()
        self.file = open(self.filename,'r')
        self.file.readline() #get rid of headers
        self.reader = csv.Reader(self.file)
