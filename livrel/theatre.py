from livrel.constant import Metres, StageDirectionTypology


class Verse:
    id: int
    text: str
    metre: Metres

    def __init__(self, id_: int, text: str, metre: Metres):

        if isinstance(id_, int):
            self.id = id_
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

    def to_dict(self):
        return vars(self)
