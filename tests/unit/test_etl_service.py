import unittest 
from unittest.mock import MagicMock
from src.application.services.etl_service import ETLService

class TestETLService(unittest.TestCase): 
    def setUp(self): 
        self.reader = MagicMock()
        self.transformer = MagicMock()
        self.writer = MagicMock()
        self.etl_service = ETLService(self.reader, self.writer, self.transformer)
    
    def test_run_success(self): 
        self.reader.read.return_value = [MagicMock()]
        self.transformer.transform.return_value = [MagicMock()]
        self.etl_service.run()
        
        self.assertEqual(self.reader.read.call_count, 1)
        self.assertEqual(self.transformer.transform.call_count, 1)
        self.assertEqual(self.writer.write.call_count, 1)

if __name__ == "__main__":
    unittest.main()

