from typing import Optional

from .constant import StageDirectionTypology, REG_S, REG_VS
from .utils import get_dict, get_variables


class Line:
    """
    Line object to analyse an actor line.
    Take a list of verses : first element need to be the character name,
    other will be multiple Verse object.
    Variables :
        character: (str) name of the character who talk
        verses: (dict) dictionary of Verse object
    :param line: (list) list of verses
    """
    def __init__(self, line: list):

        if line and len(line) > 1:
            self.character = line[0]
            self._line = line[1:]
            self.verses = {}

            self._get_verses()
        else:
            raise ValueError('line is an empty list')

    def _get_verses(self):
        for index, item in enumerate(self._line):
            self.verses[index] = Verse(item)

    def to_dict(self):
        self.verses = get_dict(self.verses)
        return get_variables(self)


class Verse:
    """
    Verse object to analyse a line.
    This will create following variables:
        text: (str) a formatted text
        stage_direction: dict(StageDirection) a dictionary of StageDirection
        type_: (str) a type of verse (v, s or vs)

    :param raw: (str) raw text of the verse
    """
    def __init__(self, raw):

        self.raw = raw
        self.text = self.raw
        self.stage_direction = {}

        self._format()
        self._get_type()

        if 's' in self.type_:
            self._format_sd()

    def _get_type(self):
        if REG_S.match(self.text):
            self.type_ = 's'
        elif REG_VS.search(self.text):
            self.type_ = 'vs'
        else:
            self.type_ = 'v'

    def _format(self):
        self.text = self.text.replace('’', '\'')

    def _format_sd(self):
        cpt = 0
        match = REG_S.search(self.text)
        for r in match.group(1).split(','):
            self.text = self.text.replace(r, '<[ stage_direction | {} ]>'.format(cpt))
            self.stage_direction[cpt] = StageDirection(r)

            cpt += 1

        self.text = self.text.replace('(', '').replace(')', '')

    def to_dict(self):
        for key in self.stage_direction.keys():
            self.stage_direction[key] = self.stage_direction[key].to_dict()
        return vars(self)


class StageDirection:
    """
    StageDirection object.
    :param text: (str) raw text of the stage direction
    :param typology: (StageDirectionTypology | None) type of the stage direction
    """
    def __init__(self, text: str, typology: Optional[StageDirectionTypology] = None):

        if isinstance(text, str):
            self.text = text
        else:
            raise ValueError('text must be an str')

        if isinstance(typology, StageDirectionTypology):
            self.typology = typology
        elif typology is None:
            self.typology = typology
        else:
            raise ValueError('typology must be a StageDirectionTypology object')

    def to_dict(self):
        return vars(self)
