import unittest
from livrel.constant import Metres, StageDirectionTypology


class TestMetres(unittest.TestCase):

    def test_monosyllabe_name(self):
        a = Metres.MONOSYLLABE
        result = 'MONOSYLLABE'
        self.assertEqual(a.name, result)

    def test_monosyllabe_value(self):
        a = Metres.MONOSYLLABE
        result = 1
        self.assertEqual(a.value, result)

    def test_monosyllabe_repr(self):
        a = Metres.MONOSYLLABE
        result = '1'
        self.assertEqual(repr(a), result)

    def test_dodecasyllabe_name(self):
        a = Metres.DODECASYLLABE
        result = 'DODECASYLLABE'
        self.assertEqual(a.name, result)

    def test_dodecasyllabe_value(self):
        a = Metres.DODECASYLLABE
        result = 12
        self.assertEqual(a.value, result)

    def test_dodecasyllabe_repr(self):
        a = Metres.DODECASYLLABE
        result = '12'
        self.assertEqual(repr(a), result)

    def test_alexandrin_name(self):
        a = Metres.ALEXANDRIN
        result = 'DODECASYLLABE'
        self.assertEqual(a.name, result)

    def test_alexandrin_value(self):
        a = Metres.ALEXANDRIN
        result = 12
        self.assertEqual(a.value, result)

    def test_alexandrin_repr(self):
        a = Metres.ALEXANDRIN
        result = '12'
        self.assertEqual(repr(a), result)

    def test_alexandrin_is_dodecasyllabe(self):
        a = Metres.ALEXANDRIN
        b = Metres.DODECASYLLABE
        self.assertIs(a, b)

    def test_unknown_NAME_error(self):
        with self.assertRaises(AttributeError):
            a = Metres.UNKNOWN_NAME
            print(a)

    def test_1_name(self):
        a = Metres(1)
        result = 'MONOSYLLABE'
        self.assertEqual(a.name, result)

    def test_1_value(self):
        a = Metres(1)
        result = 1
        self.assertEqual(a.value, result)

    def test_1_repr(self):
        a = Metres(1)
        result = '1'
        self.assertEqual(repr(a), result)

    def test_12_name(self):
        a = Metres(12)
        result = 'DODECASYLLABE'
        self.assertEqual(a.name, result)

    def test_12_value(self):
        a = Metres(12)
        result = 12
        self.assertEqual(a.value, result)

    def test_12_repr(self):
        a = Metres(12)
        result = '12'
        self.assertEqual(repr(a), result)

    def test_12_object_dodecasyllabe(self):
        a = Metres(12)
        result = Metres.DODECASYLLABE
        self.assertIs(a, result)

    def test_12_object_alexandrin(self):
        a = Metres(12)
        result = Metres.ALEXANDRIN
        self.assertIs(a, result)

    def test_unknown_value_error(self):
        with self.assertRaises(ValueError):
            Metres('UNKNOWN_VALUE')


class TestStageDirectionTypology(unittest.TestCase):

    def test_nominative_name(self):
        a = StageDirectionTypology.NOMINATIVE
        result = 'NOMINATIVE'
        self.assertEqual(a.name, result)

    def test_nominative_value(self):
        a = StageDirectionTypology.NOMINATIVE
        result = 1
        self.assertEqual(a.value, result)

    def test_nominative_repr(self):
        a = StageDirectionTypology.NOMINATIVE
        result = '1'
        self.assertEqual(repr(a), result)

    def test_1_name(self):
        a = StageDirectionTypology(1)
        result = 'NOMINATIVE'
        self.assertEqual(a.name, result)

    def test_1_value(self):
        a = StageDirectionTypology(1)
        result = 1
        self.assertEqual(a.value, result)

    def test_1_repr(self):
        a = StageDirectionTypology(1)
        result = '1'
        self.assertEqual(repr(a), result)



