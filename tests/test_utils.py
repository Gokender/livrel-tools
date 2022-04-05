from unittest import TestCase

from livrel.constant import StageDirectionTypology
import livrel.utils


class Test(TestCase):
    def test_typology_nominative_normal(self):
        a = livrel.utils.get_typology('Montrant Elmire')
        result = StageDirectionTypology.NOMINATIVE
        self.assertIs(a, result)

    def test_typology_nominative_lower(self):
        a = livrel.utils.get_typology('montrant elmire')
        result = StageDirectionTypology.NOMINATIVE
        self.assertIs(a, result)

    def test_typology_nominative_upper(self):
        a = livrel.utils.get_typology('MONTRANT ELMIRE')
        result = StageDirectionTypology.NOMINATIVE
        self.assertIs(a, result)

    def test_typology_nominative_characters(self):
        a = livrel.utils.get_typology('Donnant(\$*#Elmire.,')
        result = StageDirectionTypology.NOMINATIVE
        self.assertIs(a, result)

    def test_typology_enunciative_normal(self):
        a = livrel.utils.get_typology('à Elmire')
        result = StageDirectionTypology.ENUNCIATIVE
        self.assertIs(a, result)

    def test_typology_enunciative_upper(self):
        a = livrel.utils.get_typology('À ELMIRE')
        result = StageDirectionTypology.ENUNCIATIVE
        self.assertIs(a, result)

    def test_typology_enunciative_characters(self):
        a = livrel.utils.get_typology('à(\$*#Elmire.,')
        result = StageDirectionTypology.ENUNCIATIVE
        self.assertIs(a, result)

    def test_typology_wrong_type(self):
        with self.assertRaises(ValueError):
            livrel.utils.get_typology(18)

    def test_typology_nothing(self):
        a = livrel.utils.get_typology('Elmire')
        result = None
        self.assertIs(a, result)
