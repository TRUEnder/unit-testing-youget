import unittest
from you_get.common import *


class Match1Driver(unittest.TestCase):

    def test_return_none(self):
        text = 'https://docs.python.org/3/library/importlib.html'
        matching_str = match1(text, 'ftp://[^/]+(?:/[^/]+)*')
        self.assertEqual(matching_str, None, "Return None case failed")

    def test_return_one(self):
        text = 'https://docs.python.org/3/library/importlib.html'
        matching_str = match1(text, 'https?://([^/]+)')
        self.assertEqual(matching_str, 'docs.python.org', "Return domain case failed")

    def test_return_list(self):
        text = 'https://docs.python.org/3/library/importlib.html'
        matching_str = match1(text, 'https?://([^/]+)', 'https?://[^/]+(/.*)')
        self.assertEqual(matching_str, ['docs.python.org', '/3/library/importlib.html'], "Return list of matching string case failed")

    def test_return_empty_list(self):
        text = 'https://docs.python.org/3/library/importlib.html'
        matching_str = match1(text, 'https?://([^/]+)\.com', 'https?://[^/]+(/.*)\.php$')
        self.assertEqual(matching_str, [], "Return empty list case failed")



if __name__ == '__main__' :
    unittest.main()