from pandas import DataFrame


class DataFrameSerializer:
    def __init__(self, function, parameters=None):
        self._function = function
        self._parameters = parameters

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function):
        self._function = function

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        self._parameters = parameters

    def execute(self) -> DataFrame:
        result_set = self.function(**self.parameters) if self.parameters else self.function()
        return DataFrame.from_records(list(result_set.iterator()))
