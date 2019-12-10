class Writer:
    '''
    Writer provides class for writing data
    after tests on explain
    '''
    def __init__(self):
        pass
    
    def write(self):
        raise NotImplemented


class FileWriter(Writer):
    def __init__(self):
        super().__init__(self)
        self._path = 'explainer.exp'
    
    def write(self, data):
        f = open(self._path)
        f.write(data)
        f.close()