from unittest import TestCase

from livrel.Theatre2 import Theatre


class TestTheatre(TestCase):

    def setUp(self):
        self.theatre = Theatre(filename='test.txt', act=1)

    def test_get_lines(self):
        result = ['ACTE I', 'Scène 1', 'Bob, Alice, Thomas.', 'Bob', 'Hello World!']
        self.assertEqual(self.theatre.lines, result)

    def test_get_nb_scene(self):
        self.assertEqual(self.theatre.nb_scene, 1)

    def test_get_scene_characters(self):
        self.assertEqual(self.theatre.get_scene_characters(1), ['Bob', 'Alice', 'Thomas'])

    def test_get_act_characters(self):
        self.assertEqual(self.theatre.characters, sorted(['Bob', 'Alice', 'Thomas']))

    def test_get_scene_lines(self):
        result = {0: ['ACTE I'], 1: ['Scène 1', 'Bob, Alice, Thomas.', 'Bob', 'Hello World!']}
        self.assertEqual(self.theatre.scene_lines, result)

    def test_get_character(self):
        self.assertEqual(self.theatre.get_character('Hello World!'), (None, None))
        self.assertEqual(self.theatre.get_character('Alice, à Thomas'), ('Alice', 'à Thomas'))
        self.assertEqual(self.theatre.get_character('Bob'), ('Bob', None))
        self.assertEqual(self.theatre.get_character('Thomas, Bob'), (None, None))
        self.assertEqual(self.theatre.get_character('Alyce'), (None, None))
