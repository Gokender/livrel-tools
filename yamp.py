from collections import OrderedDict
import sys
import yaml
import io
from yaml.representer import SafeRepresenter

class LiteralString(str):
    pass


def change_style(style, representer):
    def new_representer(dumper, data):
        scalar = representer(dumper, data)
        scalar.style = style
        return scalar
    return new_representer


represent_literal_str = change_style('|', SafeRepresenter.represent_str)


yaml.add_representer(LiteralString, represent_literal_str)

markdown = """L’exemple est admirable, et cette dame est bonne !\nIl est vrai qu’elle vit en austère personne ;\nMais l’âge, dans son âme, a mis ce zèle ardent,\n"""

data2 = {'string': LiteralString(markdown)}

def str_presenter(dumper, data):
    """configures yaml for dumping multiline strings
    Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data"""
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

with io.open('books\\tartuffe\\tartuffe_1_1.yml', 'r', encoding='utf8') as infile:
    data = infile.read()

yml_data = list(yaml.load_all(data, Loader=yaml.FullLoader))
print(yml_data)

res = {}

for d in yml_data:
    print(d)

    if 'replique' in d:
        pass

yaml.add_representer(str, str_presenter)
print('----------------')
print(res)

with io.open('test_t.yml', 'w', encoding='utf8') as outfile:
    yaml.dump_all(yml_data, outfile,  indent=2, allow_unicode=True)


print(yaml.dump(data2, allow_unicode=True))



from ruamel.yaml import YAML

yaml_str = """\
short: "Hello"  # does keep the quotes, but need to tell the loader
long: |
  Line1
  Line2
  Line3
folded: >
  some like
  explicit folding
  of scalars
  for readability
"""

yaml2 = YAML()
yaml2.preserve_quotes = True

data3 = yaml2.load_all(data)

print('-'*15)
print(data3)

for d in data3:
    print(OrderedDict(d))


test = OrderedDict(
    [
        ('personnage', 'Madame Pernelle'),
        ('didascalie', OrderedDict([('text', None)])), 
        ('replique', OrderedDict(
            [
                ('text', 'Allons, Flipote, allons ; que d’eux je me délivre.\n'),
                ('didascalie', None),
                ('note', None)
            ]
            )
        )
    ]
)

test2 = [
OrderedDict([('personnage', 'Elmire'), ('didascalie', None), ('replique', dict(OrderedDict([('text', 'Vous marchez d’un tel pas, qu’on a peine à vous suivre.\n'), ('didascalie', None), ('note', None)])))]),
OrderedDict([('personnage', 'Madame Pernelle'), ('didascalie', None), ('replique', OrderedDict([('text', 'Laissez, ma bru, laissez ; ne venez pas plus loin ;\nCe sont toutes façons dont je n’ai pas besoin.\n'), ('didascalie', None), ('note', None)]))])
]

print(OrderedDict([('one', 1), ('two', 2), ('three', 3)]))

with io.open('test_t.yml', 'w', encoding='utf8') as outfile:
    #yaml.dump_all(yml_data, outfile,  indent=2, allow_unicode=True)
    yaml2.dump_all(test, outfile)
