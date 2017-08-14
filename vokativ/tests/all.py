import os
import six
import unittest

from vokativ import vokativ, sex


tests_dirname = os.path.dirname(__file__)

class VokativTest(unittest.TestCase):
    def _get_tests(self, filename):
        filename = os.path.join(tests_dirname, filename)
        tests = []
        with open(filename, 'rb') as f:
            for line in f:
                tests.append(line.decode('utf-8').split())
        return tests

    def test_basic(self):
        self.assertEqual(vokativ('Tom'), 'tome')
        self.assertEqual(vokativ('TOM'), 'tome')
        self.assertEqual(vokativ('ToM'), 'tome')
        self.assertTrue(isinstance(vokativ('Tom'), six.text_type))
        self.assertTrue(isinstance(vokativ(six.u('Tom')), six.text_type))

    def test_man_first_name(self):
        for name, vok in self._get_tests('man_first_name_tests'):
            self.assertEqual(vokativ(name, woman=False, last_name=False), vok)
            self.assertEqual(sex(name), 'm')
            self.assertEqual(vokativ(name, woman=False), vok)
            self.assertEqual(vokativ(name, last_name=False), vok)
            self.assertEqual(vokativ(name), vok)

    def test_man_last_name(self):
        for name, vok in self._get_tests('man_last_name_tests'):
            self.assertEqual(vokativ(name, woman=False, last_name=True), vok)
            self.assertEqual(sex(name), 'm')
            self.assertEqual(vokativ(name, woman=False), vok)
            self.assertEqual(vokativ(name, last_name=True), vok)
            self.assertEqual(vokativ(name), vok)

    def test_woman_first_name(self):
        for name, vok in self._get_tests('woman_first_name_tests'):
            self.assertEqual(vokativ(name, woman=True, last_name=False), vok)
            self.assertEqual(sex(name), 'w')
            self.assertEqual(vokativ(name, woman=True), vok)
            self.assertEqual(vokativ(name, last_name=False), vok)
            self.assertEqual(vokativ(name), vok)

    def test_woman_last_name(self):
        for name, vok in self._get_tests('woman_last_name_tests'):
            self.assertEqual(vokativ(name, woman=True, last_name=True), vok)
            self.assertEqual(sex(name), 'w')
            self.assertEqual(vokativ(name, woman=True), vok)
            self.assertEqual(vokativ(name, last_name=True), vok)
            self.assertEqual(vokativ(name), vok)

    def test_corner_cases(self):
        self.assertRaises(TypeError, vokativ, None)
        self.assertRaises(TypeError, vokativ, 10)
        self.assertEqual(vokativ(''), '')


if __name__ == '__main__':
    unittest.main()
