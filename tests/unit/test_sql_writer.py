import unittest
from unittest.mock import MagicMock
from src.infrastructure.writers.sql_writer import SQLWriter
from src.domain.entities.data_entity import DataEntity

class TestSQLWriter(unittest.TestCase): 
    def setUp(self): 
        self.session = MagicMock()
        self.writer = SQLWriter(self.session)

    def test_write_success(self): 
        data = [DataEntity(id=1, name="Alcie", value = 10.5)]
        self.writer.write(data)
        self.assertEqual(self.session.add.call_count, 1)
        self.assertEqual(self.session.commit.call_count, 1)

if __name__ == '__main__': 
    unittest.main()