from os import path
import six
from six.moves import cPickle as pickle


DATA_DIRNAME = path.join(path.dirname(__file__), 'data')


class Vokativ(object):
    def __init__(self, data_dirname=DATA_DIRNAME):
        self.data_dirname = data_dirname

    def vokativ(self, name, woman=None, last_name=None):
        if not isinstance(name, six.string_types):
            raise TypeError('str or unicode type expected. %s received, instead.' % type(name))
        if name == '':
            return ''
        name = six.text_type(name).lower()
        if woman is None:
            woman = self.sex(name) == 'w'
        if woman:
            if last_name is None:
                last_name = (self._get_matching_suffix(name, self.woman_f_vs_l_suffixes)[1] or 'l') == 'l'
            if last_name:
                return self._vokativ_woman_last_name(name)
            else:
                return self._vokativ_woman_first_name(name)
        else:
            return self._vokativ_man(name)

    def sex(self, name):
        name = six.text_type(name).lower()
        return self._get_matching_suffix(name, self.man_vs_woman_suffixes)[1] or 'm'

    def _vokativ_woman_first_name(self, name):
        if name[-1] == 'a':
            return name[:-1] + 'o'
        return name

    def _vokativ_woman_last_name(self, name):
        return name

    def _vokativ_man(self, name):
        suffix, vokativ_suffix = self._get_matching_suffix(name, self.man_suffixes)
        name = name[:-len(suffix)] if suffix else name
        return name + vokativ_suffix

    def _init_suffixes(self, filename):
        filename = path.join(self.data_dirname, filename)
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def _get_matching_suffix(self, name, suffixes):
        # it is important(!) to try suffixes from longest to shortest
        for suffix_length in six.moves.xrange(len(name), 0, -1):
            suffix = name[-suffix_length:]
            if suffix in suffixes:
                return (suffix, suffixes[suffix])
        return ('', suffixes.get(''))

    _man_suffixes = None
    @property
    def man_suffixes(self):
        if self._man_suffixes is None:
            self._man_suffixes = self._init_suffixes('man_suffixes')
        return self._man_suffixes

    _man_vs_woman_suffixes = None
    @property
    def man_vs_woman_suffixes(self):
        if self._man_vs_woman_suffixes is None:
            self._man_vs_woman_suffixes = self._init_suffixes('man_vs_woman_suffixes')
        return self._man_vs_woman_suffixes

    _woman_f_vs_l_suffixes = None
    @property
    def woman_f_vs_l_suffixes(self):
        if self._woman_f_vs_l_suffixes is None:
            self._woman_f_vs_l_suffixes = self._init_suffixes('woman_first_vs_last_name_suffixes')
        return self._woman_f_vs_l_suffixes


VOKATIV = Vokativ()
vokativ = VOKATIV.vokativ
sex = VOKATIV.sex
