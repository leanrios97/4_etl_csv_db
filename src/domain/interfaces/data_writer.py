from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.data_entity import DataEntity

class DataWriter(ABC): 
    @abstractmethod
    def write(self, data: List[DataEntity]) -> None: 
        """Writes a list of DataEntity objects to a persistent storage."""
        pass