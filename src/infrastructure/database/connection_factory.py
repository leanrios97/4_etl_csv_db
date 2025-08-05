from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import Settings

class ConnectionFactory: 
    def __init__(self, settings: Settings):
        self.engine = create_engine(settings.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
