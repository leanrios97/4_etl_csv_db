from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.data_entity import DataEntity

class DataTransfromer(ABC): 
    @abstractmethod
    def transform(self, data: List[DataEntity]) -> List[DataEntity]:
        """Transform a list of DataEntity objects."""
        pass
