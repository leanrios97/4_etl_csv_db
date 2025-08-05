from sqlalchemy.orm import Session
from src.domain.interfaces.data_writer import DataWriter
from src.domain.entities.data_entity import DataEntity
from src.infrastructure.database.models.data_entry_model import DataModel
from typing import List

class SQLWriter(DataWriter): 
    def __init__(self, session: Session):
        self.session = session

    def write(self, data: List[DataEntity]) -> None:
        for item in data:
            db_item = DataModel(id=item.id, name=item.name, value=item.value)
            self.session.add(db_item)
        self.session.commit()
        


