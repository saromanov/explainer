class Serializer:
    def to_json(self):
        '''
        converting of the Task object into
        JSON representation
        '''
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}