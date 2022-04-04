from livrel.theatre import Verse
from livrel.constant import Metres

#verse = Verse(1, 'Hello World!', 12)
#print(verse.to_dict())


verse = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
print(verse.to_dict())