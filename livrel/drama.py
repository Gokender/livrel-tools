from typing import Optional

from .constant import Metres, StageDirectionTypology
from .constant import REG_SD
from .utils import get_typology


class Verse:

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
        if isinstance(other, Verse):
            return self.id_ == other.id_ and self.text == other.text and self.metre == other.metre
        return False


class StageDirection:

    def __init__(self, text: str, typology: Optional[StageDirectionTypology] = None):

        self.data = text
        self._format()

        if typology is not None:
            self.typology = typology
        else:
            self.typology = get_typology(self.text)

    def to_dict(self) -> dict:
        return vars(self)

    def _format(self):
        match = REG_SD.match(self.data)
        if match:
            self.text = match.group(1)
        else:
            self.text = self.data

        self.text = self.text.replace('.', '')
        self.text = self.text.strip()

    def __eq__(self, other):
        if isinstance(other, StageDirection):
            return self.data == other.data and self.typology == other.typology
        return False
