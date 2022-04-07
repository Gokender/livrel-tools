from typing import Optional

from .constant import Metres, StageDirectionTypology


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
