import pandas as pd
import unittest 
from unittest.mock import mock_open, patch
from src.infrastructure.readers.csv_reader import CSVReader
from src.domain.entities.data_entity import DataEntity

class TestCSVReader(unittest.TestCase): 
    def setUp(self):
        self.file_path = "test.csv"
        self.reader = CSVReader(self.file_path)

    @patch("pandas.read_csv")
    def test_read_success(self, mock_read_csv): 
        mock_data = pd.DataFrame([{"id": 1, "name": "Alice", "value": 10.5}])
        mock_read_csv.return_value = mock_data
        result = self.reader.read()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, "Alice")
        self.assertEqual(result[0].value, 10.5)

if __name__ == '__main__': 
    unittest.main()