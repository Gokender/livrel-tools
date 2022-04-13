from collections import OrderedDict
from dataclasses import dataclass, field
from enum import Enum
import sys
from typing import Optional, Union
import yaml
import io
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import SingleQuotedScalarString

class WarningType(Enum):
    WRONG_TYPE = 'Wrong type for scene'

class ErrorType(Enum):
    INVALID_LITERAL = 'Invalid literal with base10'
    INVALID_STRING = 'Invalid string'

@dataclass
class Documents:
    documents: list[CommentedMap]
    correction: bool = False
    warnings: list[dict] = field(default_factory=list)
    errors: list[dict] = field(default_factory=list)

    def is_scene(self, document) -> bool:
        if 'scene' in document:
            return True
        return False

    def check(self):
        for document in self.documents:
            if self.is_scene(document):
                print('Lancement des vérifications (correction:{}) :'.format(self.correction))
                sc = Scene(document, self.warnings, self.errors, self.correction)
                sc.check_scene_type()
                sc.check_personnage_list()
                #check_scene(document, True)

@dataclass
class Result:
    obj: Optional[Union[WarningType, ErrorType]]
    expected: str
    result: str

    def to_dict(self):
        dict_res = vars(self)
        dict_res['type'] = self.obj.name
        dict_res['text'] = self.obj.value
        del dict_res['obj']
        return dict_res


@dataclass
class Scene:

    document: CommentedMap
    warnings: list[dict]
    errors: list[dict]
    correction: bool
    
    def check_scene_type(self):
        print(' - Vérification de la variable scene')
        if not isinstance(self.document['scene'], int):
            self.warnings.append(
                Result(WarningType.WRONG_TYPE, 'int', type(self.document['scene']).__name__).to_dict()
            )
            if self.correction:
                try:
                    self.document['scene'] = int(self.document['scene'])
                except ValueError as exc:
                    self.errors.append(
                        Result(ErrorType.INVALID_LITERAL, 'base10 number', self.document['scene']).to_dict()
                    )
    
    def check_personnage_list(self):
        print(' - Vérification de la liste des personnages')
        if not isinstance(self.document['personnages'], list):
            #print(type(self.document['personnages']))
            if isinstance(self.document['personnages'], str):
                if self.correction:
                    self.document['personnages'] = [self.document['personnages']]
            else:
                self.errors.append(
                    Result(ErrorType.INVALID_STRING, 'str', type(self.document['personnages']))
                )


with io.open('books\\tartuffe\\tartuffe_1_1.yml', 'r', encoding='utf8') as infile:
    data = infile.read()


yaml2 = YAML()
yaml2.preserve_quotes = True

data3 = yaml2.load_all(data)
print(data3, type(data3))

test = list(data3)

res = Result(WarningType.WRONG_TYPE, 'int', 'str')
print(res.to_dict())

cpt = 0
for t in test:
    #print(type(t))
    #print(is_scene(t))
    #if is_scene(t):
    #    check_scene(t, True)
    #t['id'] = cpt
    #print('-'*15)
    cpt += 1
    #doc = Document(t)
    #print(repr(doc))

doc = Documents(test, True)

doc.check()

print(doc.warnings)
print(doc.errors)

#test[0]['id'] = 0
#test[1]['replique']['text'] = 'bonjour\nje m\'appelle Gauthier\n'

yaml2.indent(mapping=2, sequence=2, offset=2)

with io.open('test_t.yml', 'w', encoding='utf8') as outfile:
    #yaml.dump_all(yml_data, outfile,  indent=2, allow_unicode=True)
    yaml2.dump_all(test, outfile)





test = """scene: 1
personnages: Damis
"""

plop = list(yaml2.load_all(test))
for p in plop:
    print(p)



from schema import Schema, And, Use, Optional, SchemaError


schema = Schema(
    {
        'scene':int,
        Optional('test'): list[int]
    }
)

data = {'scene':1, 'test':['gogo']}

validated = schema.validate(data)

print(validated)
###### Tests
### Scene
## scene var
# scene: 1 OK
# scene: '1' Warning OK
# scene: 1.0 + check Warning => int OK
# scene: hello warning + error KO
## personnages
# personnages : [Damis] OK
# personnages: Damis OK + warning
# personnages: [1] KO
# personnages: 1 KO


# https://github.com/pyeve/cerberus
