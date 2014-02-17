import os
import unittest

import vokativ


tests_dirname = os.path.dirname(__file__)

class VokativTest(unittest.TestCase):
    def _get_tests(self, filename):
        filename = os.path.join(tests_dirname, filename)
        tests = []
        with open(filename, 'rb') as f:
            for line in f:
                tests.append(line.decode('utf-8').split())
        return tests

    def test_test_man_first_name(self):
        for name, vok in self._get_tests('man_first_name_tests'):
            self.assertEqual(vokativ.vokativ(name, woman=False, last_name=False), vok)


if __name__ == '__main__':
    unittest.main()
