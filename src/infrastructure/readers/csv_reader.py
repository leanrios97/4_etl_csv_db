import pandas as pd
from src.domain.interfaces.data_reader import DataReader
from src.domain.entities.data_entity import DataEntity
from typing import List

class CSVReader(DataReader):
    def __init__(self, file_path: str): 
        self.file_path = file_path

    def read(self) -> List[DataEntity]:
        df = pd.read_csv(self.file_path)
        return [DataEntity(**row) for _, row in df.iterrows()]
    
    