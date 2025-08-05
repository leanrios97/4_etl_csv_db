from src.domain.interfaces.data_transformer import DataTransfromer
from src.domain.entities.data_entity import DataEntity
from typing import List

class BasicTransformer(DataTransfromer): 
    def transform(self, data: List[DataEntity]) -> List[DataEntity]:
        #Ejemplo: normalizar nombres a mayusculas y escalar valores.
        return [DataEntity(id=d.id, name=d.name.upper(), value=d.value *100) for d in data]