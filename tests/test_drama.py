from unittest import TestCase

from livrel.constant import StageDirectionTypology
from livrel.drama import Verse, StageDirection, Line


class TestVerse(TestCase):
    def test_verse_v_raw(self):
        a = Verse('Tirez de cette part, et vous, tirez de l’autre.')
        result = 'Tirez de cette part, et vous, tirez de l’autre.'
        self.assertEqual(a.raw, result)

    def test_verse_v_text(self):
        a = Verse('Tirez de cette part, et vous, tirez de l’autre.')
        result = 'Tirez de cette part, et vous, tirez de l\'autre.'
        self.assertEqual(a.text, result)

    def test_verse_v_stage_direction(self):
        a = Verse('Tirez de cette part, et vous, tirez de l’autre.')
        result = {}
        self.assertEqual(a.stage_direction, result)

    def test_verse_v_type_(self):
        a = Verse('Tirez de cette part, et vous, tirez de l’autre.')
        result = 'v'
        self.assertEqual(a.type_, result)

    def test_verse_s_raw(self):
        a = Verse('(Dorine les pousse chacun par l’épaule, et les oblige de se séparer.)')
        result = '(Dorine les pousse chacun par l’épaule, et les oblige de se séparer.)'
        self.assertEqual(a.raw, result)

    def test_verse_s_text(self):
        a = Verse('(Dorine les pousse chacun par l’épaule, et les oblige de se séparer.)')
        result = '<[ stage_direction | 0 ]>,<[ stage_direction | 1 ]>'
        self.assertEqual(a.text, result)

    def test_verse_s_stage_direction_0_text(self):
        a = Verse('(Dorine les pousse chacun par l’épaule, et les oblige de se séparer.)')
        result = 'Dorine les pousse chacun par l\'épaule'
        self.assertEqual(a.stage_direction[0].text, result)

    def test_verse_s_stage_direction_0_typology(self):
        a = Verse('(Dorine les pousse chacun par l’épaule, et les oblige de se séparer.)')
        result = None
        self.assertEqual(a.stage_direction[0].typology, result)

    def test_verse_s_type_(self):
        a = Verse('(Dorine les pousse chacun par l’épaule, et les oblige de se séparer.)')
        result = 's'
        self.assertEqual(a.type_, result)

    def test_verse_vs_raw(self):
        a = Verse('Dorine… (À Cléante.) Mon beau-frère, attendez, je vous prie.')
        result = 'Dorine… (À Cléante.) Mon beau-frère, attendez, je vous prie.'
        self.assertEqual(a.raw, result)

    def test_verse_vs_text(self):
        a = Verse('Dorine… (À Cléante.) Mon beau-frère, attendez, je vous prie.')
        result = 'Dorine… <[ stage_direction | 0 ]> Mon beau-frère, attendez, je vous prie.'
        self.assertEqual(a.text, result)

    def test_verse_vs_stage_direction_0_text(self):
        a = Verse('Dorine… (À Cléante.) Mon beau-frère, attendez, je vous prie.')
        result = 'À Cléante.'
        self.assertEqual(a.stage_direction[0].text, result)

    def test_verse_vs_stage_direction_0_typology(self):
        a = Verse('Dorine… (À Cléante.) Mon beau-frère, attendez, je vous prie.')
        result = None
        self.assertEqual(a.stage_direction[0].typology, result)

    def test_verse_vs_type_(self):
        a = Verse('Dorine… (À Cléante.) Mon beau-frère, attendez, je vous prie.')
        result = 'vs'
        self.assertEqual(a.type_, result)


# noinspection PyTypeChecker
class TestStageDirection(TestCase):

    def test_stage_direction_text(self):
        a = StageDirection('Hello')
        result = 'Hello'
        self.assertEqual(a.text, result)

    def test_stage_direction_typology_none(self):
        a = StageDirection('Hello')
        result = None
        self.assertIs(a.typology, result)

    def test_stage_direction_typology_prosodic(self):
        a = StageDirection('Hello', StageDirectionTypology.PROSODIC)
        result = 5
        self.assertEqual(a.typology, result)

    def test_stage_direction_typology_str(self):
        with self.assertRaises(ValueError):
            StageDirection('Hello', 'PROSODIC')

    def test_stage_direction_text_int(self):
        with self.assertRaises(ValueError):
            StageDirection(1)


class TestLine(TestCase):
    def test_line_empty(self):
        with self.assertRaises(ValueError):
            Line([])

    def test_line_one_element(self):
        with self.assertRaises(ValueError):
            Line(['Dorine'])

    def test_line_character(self):
        li = Line(['Dorine', 'Quel caquet est le vôtre !'])
        result = 'Dorine'
        self.assertEqual(li.character, result)

    def test_line_verses(self):
        li = Line(['Dorine', 'Quel caquet est le vôtre !'])
        self.assertIsInstance(li.verses, dict)

    def test_line_verse_object(self):
        li = Line(['Dorine', 'Quel caquet est le vôtre !'])
        self.assertIsInstance(li.verses[0], Verse)

    def test_line_verse_dict(self):
        li = Line(['Dorine', 'Quel caquet est le vôtre !'])
        li_dict = li.to_dict()
        result = 'v'
        self.assertEqual(li_dict['verses'][0]['type_'], result)
