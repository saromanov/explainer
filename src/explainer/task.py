class Task:
    ''' defines query as a task
    '''
    def __init__(self, query, times=10):
        self._query = query
        self._rows = 0
        self._times = times
    