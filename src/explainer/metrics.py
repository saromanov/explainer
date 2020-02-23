import pandas as pd
from parse import Analyzer

class Metrics:
    ''' getting analyzer objects
        for cobstruct metrics output
    '''
    def __init__(self, analyzers):
        if self._validate_input(analyzer):
            raise Execption('Metrics: unable to validate abalyzer objects')
    
        self._df = self._to_data_frame(analyzers)
    
    def _validate_input(self, data):
        ''' validating of the analyzers objects
        '''
        return len(filter(lambda x: not isinstance(x, Analyzer), data)) > 0
    
    def _to_data_frame(self, data):
        result = {}
        for x in data:
            names = x.report_names()
            report = x.report()
            for r in names:
                if r not in result:
                    result[r] = [report[r]]
                else:
                    result[r].append(result[r])
        return pd.DataFrame(result)