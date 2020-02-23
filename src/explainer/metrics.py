from typing import List
import pandas as pd
from parse import Analyzer

RawMetrics = List[Analyzer]

class Metrics:
    ''' getting analyzer objects
        for cobstruct metrics output
    '''
    def __init__(self, raw_metrics:RawMetrics):
        self._df = self._to_data_frame(raw_metrics)
    
    def _to_data_frame(self, data:RawMetrics):
        ''' converting of list of raw metrics
        to pandas data frame
        '''
        frames = []
        for tasks in data:
            result = {}
            for t in tasks:
                names = t.report_names()
                report = t.report()
                for r in names:
                    if r not in result:
                        result[r] = [report[r]]
                    else:
                        result[r].append(result[r])
            frames.append(pd.DataFrame(result))
        return frames