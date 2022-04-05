from typing import Optional

from .constant import StageDirectionTypology
from .constant import REG_NOMINATIVES_WORDS, REG_ENUNCIATIVES_WORDS


def get_typology(text: str) -> Optional[StageDirectionTypology]:
    """
    Guess the best StageDirectionTypology for a given text
    :param text: (str) text to analyse
    :return: StageDirectionTypology object or None
    """
    if not isinstance(text, str):
        raise ValueError('text must be an str')

    if REG_NOMINATIVES_WORDS.match(text.upper()):
        return StageDirectionTypology.NOMINATIVE
    elif REG_ENUNCIATIVES_WORDS.match(text.upper()):
        return StageDirectionTypology.ENUNCIATIVE
    return None
