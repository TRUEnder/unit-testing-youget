import unittest
from you_get.common import *

import types


class URLtoModuleDriver(unittest.TestCase):

    def test_valid_url(self):
        url = "https://www.youtube.com/watch?v=example_video"
        module = url_to_module(url)[0]
        self.assertIsInstance(module, types.ModuleType)

    def test_unsupported_url(self):
        with self.assertRaises():
            url = "https://unsupported-website.com/video"
            module = url_to_module(url)[0]

    def test_redirect_url(self):
        with self.assertRaises():
            url = "https://redirect.com/video"
            module = url_to_module(url)[0]


if __name__ == '__main__' :
    unittest.main()