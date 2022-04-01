import io
import re
from collections import defaultdict


class Theatre:
    def __init__(self, filename, act, encoding='utf8'):
        self.filename = filename
        self.act = act

        self.data = self.load_txt(encoding)
        self.lines = self.get_lines()
        self.nb_scene = self.get_nb_scene()
        self.characters = self.get_act_characters()
        self.scene_lines = self.get_scene_lines()

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
