import os
from livrel import Theatre

filepath = os.path.join('data', 'tartuffe_1.txt')

theatre = Theatre.Theatre(filepath, 1)

print(theatre.characters)