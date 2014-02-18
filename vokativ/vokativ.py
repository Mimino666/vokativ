from os import path
import six
from six.moves import cPickle as pickle


DATA_DIRNAME = path.join(path.dirname(__file__), 'data')


class Vokativ(object):
    def __init__(self, data_dirname=DATA_DIRNAME):
        self.data_dirname = data_dirname

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
        return self._find_correct_suffix(name, self.man_suffixes)

    def _vokativ_man_last_name(self, name):
        return self._find_correct_suffix(name, self.man_suffixes)

    def _init_suffixes(self, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def _find_correct_suffix(self, name, suffixes):
        # it is important(!) to try suffixes from longest to shortest
        for suffix_length in six.moves.xrange(len(name), 0, -1):
            suffix = name[-suffix_length:]
            if suffix in suffixes:
                return name[:-suffix_length] + suffixes[suffix]
        return name + suffixes.get('', '')

    _man_suffixes = None
    @property
    def man_suffixes(self):
        if self._man_suffixes is None:
            self._man_suffixes = self._init_suffixes(path.join(self.data_dirname, 'man_suffixes'))
        return self._man_suffixes


VOKATIV = Vokativ()
vokativ = VOKATIV.vokativ
