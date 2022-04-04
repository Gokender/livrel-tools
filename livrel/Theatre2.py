import io
import json
import re
from collections import defaultdict


class Theatre:

    def __init__(self, filename, act, encoding='utf8'):
        self.filename = filename
        self.act = act

        self.verse_id = -1
        self._temp_dict = defaultdict(dict)
        self.scene_dict = defaultdict(int)
        self.act_dict = defaultdict(dict)

        self.data = self.load_txt(encoding)
        self.lines = self.get_lines()
        self.nb_scene = self.get_nb_scene()
        self.characters = self.get_act_characters()
        self.scene_lines = self.get_scene_lines()

        self.analyse_act()
        self.save_json('test.json')


    def load_txt(self, encoding):
        with io.open(self.filename, 'r', encoding=encoding) as infile:
            datasource = infile.read()
        return datasource

    def get_lines(self):
        lines = []
        for line in self.data.splitlines():
            if line != '':
                lines.append(line)
        return lines

    def get_nb_scene(self):
        nb_scene = 0
        for line in self.lines:
            if re.match(r'Scène (\d+)', line) is not None:
                nb_scene += 1
        return nb_scene

    def get_scene_characters(self, scene):
        index = 0
        for line in self.lines:
            if re.match(r'Scène {}'.format(scene), line) is not None:
                return self.lines[index + 1].rstrip('.').split(', ')
            index += 1

    def get_act_characters(self):
        unique = []
        for i in range(1, self.nb_scene + 1):
            unique = list(set(unique + self.get_scene_characters(i)))
        return sorted(unique)

    def get_scene_lines(self):
        scene_lines = defaultdict(list)
        scene = 0
        for line in self.lines:
            match = re.match(r'Scène (\d+)', line)
            if match is not None:
                scene = match.group(1)
            scene_lines[int(scene)].append(line)
        return dict(scene_lines)

    def get_character(self, line) -> (str, str):
        charac = None
        stage_direction = None
        for character in self.characters:
            pattern = re.compile(r'({c}), (à \w+)|({c})(?!, )'.format(c=character))
            match = pattern.match(line)
            if match:
                if match.group(1) is None:
                    charac = match.group(3)
                else:
                    charac = match.group(1)
                    stage_direction = match.group(2)

        return charac, stage_direction

    def scene_lines_to_struct(self, scene):

        prec_character = ''
        index_dialogue = 0
        verses = []
        for index in range(2, len(self.scene_lines[scene])):
            line = self.scene_lines[scene][index]
            character, stage_direction = self.get_character(line)
            #print(index, len(self.scene_lines[scene]), line, character, stage_direction)

            if character is not None:
                if not prec_character == '':
                    verses_dict = self.verses_to_struct(verses)
                    self._temp_dict[index_dialogue] = dict(character=prec_character, verses=verses_dict)

                    if stage_direction is not None:
                        self._temp_dict[index_dialogue]['stage_direction'] = stage_direction

                    index_dialogue += 1

                prec_character = character
                verses = []
            elif index == len(self.scene_lines[scene])-1:
                verses.append(line)
                verses_dict = self.verses_to_struct(verses)
                self._temp_dict[index_dialogue] = dict(character=prec_character, verses=verses_dict)
            else:
                verses.append(line)

        return self._temp_dict

    def verses_to_struct(self, verses):
        verses_dict = defaultdict(dict)

        reg_noteref = r'([a-zA-Z\u00C0-\u00FF]+)(\[(\d+)\])'
        reg_stage_direction = r'\((.*?)\)'

        cpt = 0

        for verse in verses:
            #print(cpt, verse)
            match = re.match(reg_stage_direction, verse)

            if match:
                text = '<% {text} | sd %>'.format(text=match.group(1))
                verse_res = dict(text=text)
            else:
                self.verse_id += 1
                text = re.sub(reg_noteref, r'<% \1 | note_\3 %>', verse)
                verse_res = dict(id=self.verse_id, text=text)

            verses_dict[cpt] = verse_res
            cpt += 1

        return dict(verses_dict)

    def analyse_act(self):

        temp = defaultdict(dict)

        for scene in range(1, self.nb_scene-2):

            print(scene, self.get_scene_characters(scene))
            temp[scene] = dict(
                characters=self.get_scene_characters(scene),
                dialogues=self.scene_lines_to_struct(scene)
            )

        self.act_dict[self.act] = dict(
            scenes=temp
        )

    def save_json(self, filename):
        #'test.json'
        with io.open(filename, 'w', encoding='utf8') as outfile:
            json.dump(dict(self.act_dict), outfile, ensure_ascii=False, indent=2)
