import pandas as pd
from parse import Analyzer

class Metrcis:
    ''' getting analyzer objects
        for cobstruct metrics output
    '''
    def __init__(self, analyzers):
        if self._validate_input(analyzer):
            raise Execption('Metrics: unable to validate abalyzer objects')
    
    def _validate_input(self, data):
        ''' validating of the analyzers objects
        '''
        return len(filter(lambda x: not isinstance(x, Analyzer), data)) > 0