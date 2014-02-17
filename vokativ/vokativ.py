import os
import six


SUFFIXES_DIRNAME = os.path.join(os.path.dirname(__file__), 'suffixes')


class Vokativ(object):
    def __init__(self, suffixes_dirname=SUFFIXES_DIRNAME):
        self.suffixes_dirname = suffixes_dirname
        self._man_first_name_suffixes = None
        self._man_last_name_suffixes = None

    def vokativ(self, name, woman=False, last_name=False):
        if not isinstance(name, six.string_types):
            raise TypeError('str or unicode type expected. %s received, instead.' % type(name))
        name = six.text_type(name).lower()
        if not name:
            return name

        if woman:
            if last_name:
                return self._vokativ_woman_last_name(name)
            else:
                return self._vokativ_woman_first_name(name)
        else:
            if last_name:
                return self._vokativ_man_last_name(name)
            else:
                return self._vokativ_man_first_name(name)

    def _vokativ_woman_first_name(self, name):
        if name[-1] == 'a':
            return name[:-1] + 'o'
        return name

    def _vokativ_woman_last_name(self, name):
        return name

    def _vokativ_man_first_name(self, name):
        if self._man_first_name_suffixes is None:
            filename = os.path.join(self.suffixes_dirname, 'man_first_name')
            self._man_first_name_suffixes = self._init_suffixes(filename)
        return self._find_correct_suffix(self._man_first_name_suffixes, name) or (name + 'e')

    def _vokativ_man_last_name(self, name):
        if self._man_last_name_suffixes is None:
            filename = os.path.join(self.suffixes_dirname, 'man_last_name')
            self._man_last_name_suffixes = self._init_suffixes(filename)
        return self._find_correct_suffix(self._man_last_name_suffixes, name) or (name + 'e')

    def _init_suffixes(self, filename):
        suffixes = {}
        with open(filename, 'rb') as f:
            for line in f:
                tokens = line.decode('utf-8').split()
                suffixes[tokens[0]] = tokens[1]
        return suffixes

    def _find_correct_suffix(self, suffixes, name):
        # it is important(!) to try suffixes from longest to shortest
        for suffix_length in six.moves.xrange(len(name), 0, -1):
            suffix = name[-suffix_length:]
            if suffix in suffixes:
                return name[:-suffix_length] + suffixes[suffix]


VOKATIV = Vokativ()
vokativ = VOKATIV.vokativ
