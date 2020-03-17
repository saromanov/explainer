from typing import List, Dict
import pandas as pd
from parse import Analyzer
from task import Task
from serializer import Serializer

RawMetrics = List[Analyzer]
Tasks = List[Task]

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
    
    def __getitem__(self, name) -> pd.DataFrame:
       return self._data[name]
    
    def __str__(self) -> str:
        return 'Number of tasks: {0}'.format(len(self._data))
    
    def stat(self, name) -> Dict[str, float]:
        '''
        return of the basic statistics about execution
        '''
        return {'mean': self.mean(name), 'median': self.median(name)}
    
    def _apply_stat(self, name, func, *args, **kwargs) -> float:
        '''
        general method for applying stats methods
        from pandas data frame
        '''
        task = kwargs.get('task')
        if not task:
            raise Exception('task name is not defined')
        return getattr(self._data[task][name], func)()
    
    def median(self, name, *args, **kwargs) -> float:
        ''' return median value from results
        '''
        return self._apply_stat(name, 'median', *args, **kwargs)
    
    def mean(self, name, *args, **kwargs) -> float:
        ''' return mean value from results
        '''
        return self._apply_stat(name, 'mean',  *args, **kwargs)
    
    def std(self, name, *args, **kwargs) -> float:
        ''' return std value from results
        '''
        return self._apply_stat(name, 'std',  *args, **kwargs)


class MetricsStore(Serializer):
    def __init__(self, task_name, metric_names, method_names, metric:Metrics, task:Task, /):
        self.task_name = task_name
        self.metrics = self._set_metrics(metric_names, method_names, metric, task)
    
    def _set_metrics(self, metric_names, method_names, metrics:Metrics, task:Task):
        result = {}
        for m in metric_names:
            for method_name in method_names:
                result[f'{method_name}'] = getattr(metrics, method_name)(m, task=task)
        return result
    



def from_csv(path) -> pd.DataFrame:
    return pd.read_csv(path)