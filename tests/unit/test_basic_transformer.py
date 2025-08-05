import unittest
from src.infrastructure.transformers.basic_transformer import BasicTransformer
from src.domain.entities.data_entity import DataEntity

class TestBasicTransformer(unittest.TestCase): 
    def setUp(self):
        self.transformer = BasicTransformer()
    
    def test_transformer_success(self): 
        input_data = [DataEntity(id=1, name="Alice", value=10.5)]
        result = self.transformer.transform(input_data)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, "ALICE")
        self.assertEqual(result[0].value, 10.5 * 100)

if __name__ == '__main__': 
    unittest.main()