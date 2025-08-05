# scripts\run_etl.py
from src.application.services.etl_service import ETLService
from src.infrastructure.readers.csv_reader import CSVReader
from src.infrastructure.writers.sql_writer import SQLWriter
from src.infrastructure.transformers.basic_transformer import BasicTransformer
from src.infrastructure.database.connection_factory import ConnectionFactory
from src.config.settings import Settings

def main():
    settings = Settings()
    reader = CSVReader(settings.csv_file_path)
    transformer = BasicTransformer()
    connection_factory = ConnectionFactory(settings)
    writer = SQLWriter(connection_factory.get_session())
    etl_service = ETLService(reader, writer, transformer)
    etl_service.run()

if __name__ == "__main__":
    main()