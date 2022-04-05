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


a = Metres(1)
a = Metres(12)
print(a)
print(a is Metres.DODECASYLLABE)
print(a is Metres.ALEXANDRIN)
print(type(a)) #isInstance
#print(Metres(13)) # Value error
#print(Metres('toto')) # Value error

class StageDirectionTypology(enum.Enum):
    NOMINATIVE = 1  # Designating a character
    ENUNCIATIVE = 2  # To whom a character is speaking
    LOCATIVE = 3  # Indicate the place of the action;
    KINESIC = 4

    def __repr__(self) -> str:
        return str(self.value)


class Verse:
    id_: int
    text: str
    metre: Metres

    def __init__(self, id_: int, text: str, metre: Metres):

        if isinstance(id_, int):
            self.id_ = id_
        else:
            raise ValueError('id_ must be an int')

        if isinstance(text, str):
            self.text = text
        else:
            raise ValueError('text must be an str')

        if isinstance(metre, Metres):
            self.metre = metre
        else:
            raise ValueError('metre must be an Metres object')

    def to_dict(self) -> dict:
        return vars(self)

    def __eq__(self, other):
        if (isinstance(other, Verse)):
            return self.id_ == other.id_ and self.text == other.text and self.metre == other.metre
        return False



a = Verse(1, 'Hello World!', Metres.ALEXANDRIN) # True
b = Verse(1, 'Hello World!', Metres.DODECASYLLABE)
#verse = Verse(1, 'Hello World!', Metres.ALEXANDRIN) # True a == b
#verse = Verse('Hello', 'World!', Metres.ALEXANDRIN) # False ValueError id_ must be an int
#verse = Verse(1, 18, Metres.ALEXANDRIN) # False ValueError text must be an str
#verse = Verse(1, 'Hello World!', 12) # False ValueError metre must be an Metres object
#verse = Verse(1, 'Hello World!', Metres.ALEXANDRIN) # True {'id_': 1, 'text': 'Hello World!', 'metre': 12}
#verse = Verse()
print(a.metre)
print(a.to_dict())
print(a == b)






sd = StageDirection('(Montrant Cléante.)', StageDirectionTypology.NOMINATIVE)
print(sd.to_dict())

tests = ['(À Elmire.)','(Donnant un soufflet à Flipote.)','(Montrant Cléante. )','à Elmire.','(Montrant Elmire.)']

sd = StageDirection('(Montrant Cléante. )', StageDirectionTypology.NOMINATIVE)
print(sd.to_dict())
sd = StageDirection('( Montrant Cléante. )', StageDirectionTypology.NOMINATIVE)
print(sd.to_dict())
sd = StageDirection('à Elmire.', StageDirectionTypology.NOMINATIVE)
print(sd.to_dict())




print(REG_NOMINATIVES_WORDS.match('Montrant Cléante'.upper()))
print(REG_ENUNCIATIVES_WORDS.match('à Elmire'.upper()))

def get_typology(text: str) -> StageDirectionTypology:

    if not isinstance(text, str):
        raise ValueError('text must be an str')

    if REG_NOMINATIVES_WORDS.match(text.upper()):
        return StageDirectionTypology.NOMINATIVE
    elif REG_ENUNCIATIVES_WORDS.match(text.upper()):
        return StageDirectionTypology.ENUNCIATIVE
    return None

print(get_typology('Montrant Cléante'))
print(get_typology(1))

print(Metres.ALEXANDRIN.name)
