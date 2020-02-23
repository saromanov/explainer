from typing import List, Dict

class Analyzer:
    def __init__(self):
        self.planning_time = ''
        self.execution_time = ''
        self._sort_names = []
        self._tasks = []
    
    def report(self) -> Dict[str, str]:
        return {'planning_time': self.planning_time, 'execution_time': self.execution_time}
    
    def report_names(self) -> List[str]:
        return ['planning_time', 'execution_time']

def parse_explain(value) -> Analyzer:
    an = Analyzer()
    check_start = lambda x, y: x.startswith(y)
    sort_names = lambda x: x.split(',')
    get_time = lambda x: x.split(':')[1]
    for v in value:
        data = v[0]
        if check_start(data, 'Planning'):
            an.planning_time = get_time(data)
        if check_start(data, 'Execution'):
            an.execution_time = get_time(data)
        if check_start(data, 'Sort Key'):
            an.sort_names = sort_names(data)
    return an