import os
from livrel import Theatre

filepath = os.path.join('data', 'tartuffe_1.txt')
#filepath = os.path.join('data', 'test.txt')

theatre = Theatre.Theatre(filepath, 1)

#print(theatre.nb_scene)
#print(theatre.characters)

#theatre.scene_lines_to_struct(1)

verses = [
    'Voilà les contes bleus qu’il vous faut pour vous plaire,',
    'Ma bru. L’on est chez vous contrainte de se taire :',
    'Car madame, à jaser, tient le dé tout le jour.',
    'Mais enfin je prétends discourir à mon tour :',
    'Je vous dis que mon fils n’a rien fait de plus sage',
    'Qu’en recueillant chez soi ce dévot personnage ;',
    'Que le ciel au besoin l’a céans envoyé',
    'Pour redresser à tous votre esprit fourvoyé ;',
    'Que, pour votre salut, vous le devez entendre,',
    'Et qu’il ne reprend rien qui ne soit à reprendre.',
    'Ces visites, ces bals, ces conversations,',
    'Sont du malin esprit toutes inventions.',
    'Là, jamais on n’entend de pieuses paroles ;',
    'Ce sont propos oisifs, chansons, et fariboles :',
    'Bien souvent le prochain en a sa bonne part,',
    'Et l’on y sait médire et du tiers et du quart.',
    'Enfin les gens sensés ont leurs têtes troublées',
    'De la confusion de telles assemblées :',
    'Mille caquets divers s’y font en moins de rien ;',
    'Et, comme l’autre jour un docteur dit fort bien,',
    'C’est véritablement la tour de Babylone[9],',
    'Car chacun y babille, et tout du long de l’aune[10] ;',
    'Et, pour conter l’histoire où ce point l’engagea…',
    '(Montrant Cléante.)',
    'Voilà-t-il pas monsieur qui ricane déjà !',
    'Allez chercher vos fous qui vous donnent à rire,',
    '(À Elmire.)',
    'Et sans… Adieu, ma bru ; je ne veux plus rien dire.',
    'Sachez que pour céans j’en rabats de moitié,',
    'Et qu’il fera beau temps quand j’y mettrai le pied.',
    '(Donnant un soufflet à Flipote.)',
    'Allons, vous, vous rêvez et bayez aux corneilles.',
    'Jour de Dieu ! je saurai vous frotter les oreilles.',
    'Marchons, gaupe, marchons[11].'
]
print('------------------------------')
#theatre.verses_to_struct(verses)


#theatre.analyse_act()