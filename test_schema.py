import unittest

from ruamel.yaml import YAML
from cerberus import Validator

from schema import schema_text, schema_stage_direction

class TestSchemaDialogue(unittest.TestCase):

    def setUp(self) -> None:
        self.yaml = YAML()
        self.yaml.preserve_quotes = True

        self.v = Validator()

    def test_schema_texte_true(self):
        data = """texte: |
          Laissez, ma bru, laissez ; ne venez pas plus loin ;
          Ce sont toutes façons dont je n’ai pas besoin.
        """

        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_text)

        self.assertEqual(result, True)
        self.assertEqual(self.v.errors, {})

    def test_schema_texte_no(self):
        data = """test: |
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_text)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['texte'], ['required field'])
        self.assertEqual(self.v.errors['test'], ['unknown field'])

    def test_schema_texte_empty(self):
        data = """texte: |

        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_text)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['texte'], ['empty values not allowed'])

    def test_schema_texte_none(self):
        data = """texte:"""
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_text)

        #print(dict(yaml_data[0]), self.v.errors, result)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['texte'], ['null value not allowed'])
    
    def test_schema_didascalie_true(self):
        data = """didascalie: 
          - 
            texte: didascalie_1
            typologie: test_1
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        self.assertEqual(result, True)
        self.assertEqual(self.v.errors, {})

    def test_schema_didascalie_unknown(self):
        data = """didascalie: 
          - 
            test: didascalie_1
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['didascalie'][0][0][0]['test'], ['unknown field'])
    
    def test_schema_didascalie_wtho_typology_true(self):
        data = """didascalie: 
          - 
            texte: didascalie_1
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        self.assertEqual(result, True)
        self.assertEqual(self.v.errors, {})

    def test_schema_didascalie_texte_none(self):
        data = """didascalie: 
          - 
            texte: 
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        self.assertEqual(result, True)
        self.assertEqual(self.v.errors, {})

    def test_schema_didascalie_texte_empty(self):
        data = """didascalie: 
          - 
            texte: ''
        """
      
        yaml_data = list(self.yaml.load_all(data))
        #print(yaml_data)
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        #print(self.v.errors, result)
        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['didascalie'][0][0][0]['texte'], ['empty values not allowed'])

    def test_schema_didascalie_typology_wtho_texte(self):
        data = """didascalie: 
          - 
            typologie: test_1
        """
      
        yaml_data = list(self.yaml.load_all(data))
        #print(yaml_data)
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        #print(self.v.errors, result)
        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['didascalie'][0][0][0]['typologie'], ['field \'texte\' is required'])

    def test_schema_didascalie_typology_none(self):
        data = """didascalie: 
          - 
            texte: didascalie_1
            typologie: 
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        self.assertEqual(result, True)
        self.assertEqual(self.v.errors, {})

    def test_schema_didascalie_list_none(self):
        data = """didascalie: 
          - 
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        #print(dict(yaml_data[0]))
        #print(self.v.errors, result)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['didascalie'][0][0], ['null value not allowed'])
    
    def test_schema_didascalie_none(self):
        data = """didascalie: 
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        #print(dict(yaml_data[0]))
        #print(self.v.errors, result)

        self.assertEqual(result, True)
        self.assertEqual(self.v.errors, {})
    
    def test_schema_didascalie_empty(self):
        data = """didascalie: []
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        #print(dict(yaml_data[0]))
        #print(self.v.errors, result)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['didascalie'], ['empty values not allowed'])

    def test_schema_didascalie_string(self):
        data = """didascalie: test
        """
      
        yaml_data = list(self.yaml.load_all(data))
        result = self.v.validate(yaml_data[0], schema_stage_direction)

        #print(dict(yaml_data[0]))
        #print(self.v.errors, result)

        self.assertEqual(result, False)
        self.assertEqual(self.v.errors['didascalie'], ['must be of list type'])

if __name__ == '__main__':
    unittest.main()
