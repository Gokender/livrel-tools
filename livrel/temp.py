import enum

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
    NOMINATIVE = 1 #Designating a character
    ENUNCIATIVE = 2 #To whom a character is speaking
    LOCATIVE = 3 #Indicate the place of the action;
    KINESIC = 4

    def __repr__(self) -> str:
        return str(self.value)


print (Metres.MONOSYLLABE.value)
print (repr(Metres.TRISYLLABE))

print(Metres.DODECASYLLABE)
print(Metres.ALEXANDRIN)


from collections import defaultdict

class Theatre:
    def __init__(self):
        self.filename = 'test.txt'
        self.name = 'Test'

        self.acts = []
    
    def act(self, id: int):
        if id > 0:
            return self.acts[id-1]

class Scene:
    no: int = None
    characters: list = None
    description: str = None

    def __init__(self, no, characters=None, description=None):
        self.no = no
        self.characters = characters
        self.description = description

class Act:
    no: int = None
    characters: list = None
    description: str = None
    scenes: list

    def __init__(self, no, characters=None, description=None):
        self.no = no
        self.characters = characters
        self.description = description

        self.scenes = []

theatre = Theatre()
theatre.acts.append(Act(1))
print(theatre.acts)

theatre.acts[0].scenes.append(Scene(1, characters=['Gogo']))
theatre.acts[0].scenes.append(Scene(2, characters=['Lauri']))

for scene in theatre.acts[0].scenes:
    print(scene.characters)

for scene in theatre.act(1).scenes:
    print(scene.characters)


from collections import defaultdict
from test2 import Metres, StageDirectionTypology

class Verse:
    id: int
    text: str
    metre: Metres

    def __init__(self, id, text, metre):

        self.id = id
        self.text = text
        self.metre = metre

    def to_dict(self):
        return vars(self)


verse = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
print(verse.to_dict())


class StageDirection:

    text: str
    typology: StageDirectionTypology

    def __init__(self, text, typology):

        self.text = text
        self.typology = typology

    def to_dict(self):
        return vars(self)

sd = StageDirection('Montrant Cléante', StageDirectionTypology.NOMINATIVE)
print(sd.to_dict())


class Noteref:

    def __init__(self, word, id, text=None):

        self.word = word
        self.id = id
        self.text = text

    def to_dict(self):
        return vars(self)

noteref = Noteref('marchons', 11, 'blabla')
print(noteref.to_dict())

noteref = Noteref('marchons', 11)
print(noteref.to_dict())

class Line:

    character: str
    stage_direction: StageDirection

    def __init__(self, character, stage_direction=None):

        self.character = character
        self.stage_direction = stage_direction

        self._id = 0
        self.verses = {}
        self._update_stats()

    def add(self, obj):
        self.verses[self.nb_elements] = obj
        self._update_stats()

    def _update_stats(self):
        cpt = 0
        for key in self.verses.keys():
            if isinstance(self.verses[key], Verse):
                cpt += 1
        
        self.nb_elements = len(self.verses.keys())
        self.nb_verses = cpt

    def _verses_to_dict(self):
        for key in self.verses.keys():
            self.verses[key] = self.verses[key].to_dict()

    def to_dict(self):
        self._verses_to_dict()
        return vars(self)


line = Line('Dorine')
print(line.to_dict())

verse = Verse(0, 'Allons, vous, vous rêvez et bayez aux corneilles.', Metres.ALEXANDRIN)
line.add(verse)
verse = Verse(1, 'Et sans… Adieu, ma bru ; je ne veux plus rien dire.', Metres.ALEXANDRIN)
line.add(verse)
verse = StageDirection('Montrant Cléante', StageDirectionTypology.NOMINATIVE)
line.add(verse)

print(line.to_dict())


test = """Et, pour conter l’histoire où ce point l’engagea…
(Montrant Cléante.)
Voilà-t-il pas monsieur qui ricane déjà !
Allez chercher vos fous qui vous donnent à rire,
(À Elmire.)
Et sans… Adieu, ma bru ; je ne veux plus rien dire.
Sachez que pour céans j’en rabats de moitié,
Et qu’il fera beau temps quand j’y mettrai le pied.
(Donnant un soufflet à Flipote.)
Allons, vous, vous rêvez et bayez aux corneilles.
Jour de Dieu ! je saurai vous frotter les oreilles.
Marchons, gaupe, marchons[11].
"""

cpt = 0
line = Line('Madame Pernelle')
for t in test.splitlines():
    #print(t)
    verse = Verse(cpt, t, Metres.ALEXANDRIN)
    line.add(verse)
    cpt += 1

line.add(StageDirection('Donnant un soufflet à Flipote', StageDirectionTypology.NOMINATIVE))
print(line.to_dict())
