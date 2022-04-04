import unittest
from livrel.theatre import Verse
from livrel.constant import Metres


class TestVerse(unittest.TestCase):

    def test_something(self):

        print(Metres.ALEXANDRIN)

        verse = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
        print(verse)

        verse = Verse(1.0, 3, ' ')
        print(verse.to_dict())

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
