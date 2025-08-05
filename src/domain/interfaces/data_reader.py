from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.data_entity import DataEntity

class DataReader(ABC): 
    @abstractmethod
    def read(self) -> List[DataEntity]:
        """Reads data and returns a list of DataEntity objects."""
        pass