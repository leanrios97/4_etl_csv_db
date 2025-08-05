from src.domain.interfaces.data_reader import DataReader
from src.domain.interfaces.data_writer import DataWriter
from src.domain.interfaces.data_transformer import DataTransfromer

class ETLService:
    def __init__(self, reader: DataReader, writer: DataWriter, transformer: DataTransfromer):
        self.reader = reader
        self.writer = writer
        self.transformer = transformer

    def run(self):
        data = self.reader.read()
        transformed_data = self.transformer.transform(data)
        self.writer.write(transformed_data)