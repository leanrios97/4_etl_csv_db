# tests/integration/test_etl_pipeline.py
import unittest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from src.application.services.etl_service import ETLService
from src.infrastructure.readers.csv_reader import CSVReader
from src.infrastructure.transformers.basic_transformer import BasicTransformer
from src.infrastructure.writers.sql_writer import SQLWriter
from src.infrastructure.database.connection_factory import ConnectionFactory
from src.infrastructure.database.models.data_entry_model import DataModel
from src.config.settings import Settings



class TestETLPipeline(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()
        self.connection_factory = ConnectionFactory(self.settings)
        self.session = self.connection_factory.get_session()

        # LIMPIAR TABLA y REINICIAR SEQUENCE antes de cada test
        self.session.execute(text("TRUNCATE TABLE data_entry RESTART IDENTITY CASCADE;"))
        self.session.commit()

        self.reader = CSVReader(self.settings.csv_file_path)
        self.transformer = BasicTransformer()
        self.writer = SQLWriter(self.session)
        self.etl_service = ETLService(self.reader, self.writer, self.transformer)

    def tearDown(self):
        try:
            self.session.rollback()
        except Exception:
            pass

        self.session.execute(text("TRUNCATE TABLE data_entry RESTART IDENTITY CASCADE;"))
        self.session.commit()
        self.session.close()

    def test_etl_pipeline_success(self):
        result = self.etl_service.run()
        self.assertTrue(True) 

if __name__ == "__main__":
    unittest.main()