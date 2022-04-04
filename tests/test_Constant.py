import unittest
from livrel.constant import Metres, StageDirectionTypology


class TestMetres(unittest.TestCase):
    def test_name_monosyllabe(self):
        metre = Metres.MONOSYLLABE
        result = 'MONOSYLLABE'
        self.assertEqual(metre.name, result)

    def test_name_quadrisyllabe(self):
        metre = Metres.QUADRISYLLABE
        result = 'TETRASYLLABE'
        self.assertEqual(metre.name, result)

    def test_name_alexandrin(self):
        metre = Metres.ALEXANDRIN
        result = 'DODECASYLLABE'
        self.assertEqual(metre.name, result)

    def test_value_monosyllabe(self):
        metre = Metres.MONOSYLLABE
        result = 1
        self.assertEqual(metre.value, result)

    def test_value_quadrisyllabe(self):
        metre = Metres.QUADRISYLLABE
        result = 4
        self.assertEqual(metre.value, result)

    def test_value_tetrasyllabe(self):
        metre = Metres.TETRASYLLABE
        result = 4
        self.assertEqual(metre.value, result)

    def test_instance_monosyllabe(self):
        metre = Metres.MONOSYLLABE
        self.assertIsInstance(metre, Metres)

    def test_instance_quadrisyllabe(self):
        metre = Metres.QUADRISYLLABE
        self.assertIsInstance(metre, Metres)

    def test_instance_tetrasyllabe(self):
        metre = Metres.TETRASYLLABE
        self.assertIsInstance(metre, Metres)


class TestStageDirectionTypology(unittest.TestCase):

    def test_name_enunciative(self):
        stage = StageDirectionTypology.ENUNCIATIVE
        result = 'ENUNCIATIVE'
        self.assertEqual(stage.name, result)


if __name__ == '__main__':
    unittest.main()
