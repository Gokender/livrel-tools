import enum
import re


class Metres(enum.IntEnum):
    MONOSYLLABE = 1
    DISSYLLABE = 2
    TRISYLLABE = 3
    TETRASYLLABE = 4
    QUADRISYLLABE = 4
    PENTASYLLABE = 5
    HEXASYLLABE = 6
    HEPTASYLLABE = 7
    OCTOSYLLABE = 8
    ENNEASYLLABE = 9
    DECASYLLABE = 10
    HENDECASYLLABE = 11
    DODECASYLLABE = 12
    ALEXANDRIN = 12

    def __repr__(self) -> str:
        return str(self.value)


class StageDirectionTypology(enum.Enum):
    NOMINATIVE = 1  # Designating a character
    ENUNCIATIVE = 2  # To whom a character is speaking
    LOCATIVE = 3  # Indicate the place of the action;
    KINESIC = 4

    def __repr__(self) -> str:
        return str(self.value)


NOMINATIVES_WORDS = [
    'Montrant',
    'Donnant'
]

ENUNCIATIVES_WORDS = [
    'à'
]

REG_NOMINATIVES_WORDS = re.compile(r'|'.join(word.upper() for word in NOMINATIVES_WORDS))
REG_ENUNCIATIVES_WORDS = re.compile(r'|'.join(word.upper() for word in ENUNCIATIVES_WORDS))
