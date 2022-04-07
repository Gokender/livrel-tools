from unittest import TestCase

from livrel.constant import StageDirectionTypology
from livrel.utils import get_variables, get_dict


class TestVar:
    def __init__(self):
        self.a = 1
        self._b = 1
        self.a_ = 1
        self.a_a = 1
        self._1 = 1

    def to_dict(self):
        return vars(self)


class TestDict:
    def __init__(self):
        self.c = {0: TestVar()}


class TestGetVariables(TestCase):
    def setUp(self) -> None:
        self.t = TestVar()

    def test_get_variables_a(self):
        result = get_variables(self.t)
        self.assertEqual(self.t.a, 1)
        self.assertIn('a', result)

    def test_get_variables__b(self):
        result = get_variables(self.t)
        self.assertNotIn('_b', result)

    def test_get_variables_a_(self):
        result = get_variables(self.t)
        self.assertEqual(self.t.a_, 1)
        self.assertIn('a_', result)

    def test_get_variables_a_a(self):
        result = get_variables(self.t)
        self.assertEqual(self.t.a_a, 1)
        self.assertIn('a_a', result)

    def test_get_variables__1(self):
        result = get_variables(self.t)
        self.assertNotIn('_1', result)


class TestGetDict(TestCase):

    def setUp(self) -> None:
        self.t = TestDict()

    def test_get_dict_object(self):
        self.assertIsInstance(self.t.c[0], TestVar)

    def test_get_dict_dict(self):
        result = {0: {'a': 1, '_b': 1, 'a_': 1, 'a_a': 1, '_1': 1}}
        self.assertEqual(get_dict(self.t.c), result)
