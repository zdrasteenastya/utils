class TraceBlock:
    def message(self, arg):
        print ['runnig', arg]

    def __enter__(self):
        print 'starting block'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print 'All ok'
        else:
            print ['exeption', exc_type]
            return False  # raise error again


with TraceBlock() as action:
    action.message(1)
    # raise TypeError


# Work with file

class MyFile(object):

    def __init__(self, name, method):
        self.file_obj = open(name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
