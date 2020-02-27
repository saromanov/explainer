from typing import List
import pandas as pd
from parse import Analyzer

RawMetrics = List[Analyzer]

class Metrics:
    ''' getting analyzer objects
        for cobstruct metrics output
    '''
    def __init__(self, raw_metrics:RawMetrics):
        self._dframes = self._to_data_frame(raw_metrics)
    
    def _to_data_frame(self, data:RawMetrics):
        ''' converting of list of raw metrics
        to pandas data frame
        '''
        frames = []
        for tasks in data:
            result = {}
            name = 'default'
            for t in tasks:
                names = t.report_names()
                report = t.report()
                name = t.title_name()
                for r in names:
                    if r not in result:
                        result[r] = [report[r]]
                    else:
                        result[r].append(report[r])
            df = pd.DataFrame(result)
            df.name = name
            frames.append(df)
        return frames
    
    def stat(self, name):
        '''
        return of the basic statistics about execution
        '''
        return {'mean': self.mean(name), 'median': self.median(name)}
    
    def _apply_stat(self, name, func):
        '''
        general method for applying stats methods
        from pandas data frame
        '''
        result = {}
        for df in self._dframes:
            result[df.name] = getattr(df[name], func)()
        return result
    
    def median(self, name):
        ''' return median value from results
        '''
        return self._apply_stat(name, 'median')
    
    def mean(self, name):
        ''' return mean value from results
        '''
        return self._apply_stat(name, 'mean')
    
    def std(self, name):
        ''' return std value from results
        '''
        return self._apply_stat(name, 'std')


def from_cxv(path) -> pd.DataFrame:
    return pd.read_csv(path)