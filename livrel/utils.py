from typing import Optional

from .constant import StageDirectionTypology
from .constant import REG_NOMINATIVES_WORDS, REG_ENUNCIATIVES_WORDS, REG_PRIVATE_VAR


def get_variables(object_: object) -> dict:
    """
    Get all variables of an object except privates ones
    :param object_: (object) object to analyse
    :return: (dict) dictionary of variables
    """
    variables = vars(object_)
    for key in list(variables.keys()):
        if REG_PRIVATE_VAR.match(key):
            del variables[key]
    return variables


def get_dict(sub_dict: dict) -> dict:
    """
    Getting the dict for a child object
    :param sub_dict: (dict) dictionary of children in object
    :return: (dict) dictionary of children in dict
    """
    for key in sub_dict.keys():
        sub_dict[key] = sub_dict[key].to_dict()
    return sub_dict


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


def is_stage_direction(text: str) -> bool:
    return True
