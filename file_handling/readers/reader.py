from pathlib import Path
from abc import ABC, abstractmethod

import pandas as pd
from pandas import DataFrame


class BaseReader(ABC):
    @abstractmethod
    def to_dataframe(self) -> DataFrame:
        pass

    @abstractmethod
    def set_file_path(self, file_path: Path):
        pass

    @abstractmethod
    def set_reader_config(self, config: dict):
        pass


class CsvReader(BaseReader):
    def __init__(self):
        self.file_path = None
        self.config = {}

    def set_file_path(self, file_path: Path):
        self.file_path = file_path

    def set_reader_config(self, config: dict):
        self.config = config

    def to_dataframe(self) -> DataFrame:
        return pd.read_csv(self.file_path, **self.config)


class ExcelReader(BaseReader):
    def __init__(self):
        self.file_path = None
        self.config = {}

    def set_file_path(self, file_path: Path):
        self.file_path = file_path

    def set_reader_config(self, config: dict):
        self.config = config

    def to_dataframe(self) -> DataFrame:
        return pd.read_excel()
