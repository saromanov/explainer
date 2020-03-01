from typing import List
import pandas as pd
from parse import Analyzer

RawMetrics = List[Analyzer]

class Metrics:
    ''' getting analyzer objects
        for cobstruct metrics output
    '''
    def __init__(self, raw_metrics:RawMetrics):
        self._dframes, self._data = self._to_data_frame_and_dict(raw_metrics)
    
    def _to_data_frame_and_dict(self, data:RawMetrics):
        ''' converting of list of raw metrics
        to pandas data frame and dictionary
        '''
        frames = []
        data_resp = {}
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
            data_resp[name] = df
        return frames, data_resp
    
    def __getitem__(self, name):
       return self._data[name]
    
    def __str__(self):
        return 'Number of tasks: {0}'.format(len(self._data))
    
    def stat(self, name):
        '''
        return of the basic statistics about execution
        '''
        return {'mean': self.mean(name), 'median': self.median(name)}
    
    def _apply_stat(self, name, func, *args, **kwargs):
        '''
        general method for applying stats methods
        from pandas data frame
        '''
        result = {}
        task = kwargs.get('task')
        if task: 
            result[task] = getattr(df[task], func)()
        for df in self._dframes:
            result[df.name] = getattr(df[name], func)()
        return result
    
    def median(self, name, *args, **kwargs):
        ''' return median value from results
        '''
        return self._apply_stat(name, 'median', *args, **kwargs)
    
    def mean(self, name, *args, **kwargs):
        ''' return mean value from results
        '''
        return self._apply_stat(name, 'mean',  *args, **kwargs)
    
    def std(self, name, *args, **kwargs):
        ''' return std value from results
        '''
        return self._apply_stat(name, 'std',  *args, **kwargs)


def from_csv(path) -> pd.DataFrame:
    return pd.read_csv(path)