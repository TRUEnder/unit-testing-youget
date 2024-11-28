import unittest
from you_get.common import *

import http.client
import socket
import urllib.error

class UrlOpenRetryDriver(unittest.TestCase):
    
    def test_normal_url(self):
        url = 'https://www.wikipedia.org/'
        req = request.Request(url)
        res = urlopen_with_retry(req)

        self.assertIsInstance(res, http.client.HTTPResponse)
        self.assertEqual(res.status, 200)  # Assert it's not an error code
        self.assertNotIn(res.status, range(400, 600))  # Explicitly assert no error code

    def test_timeout_url(self):
        with self.assertRaises(urllib.error.HTTPError):
            url = 'http://httpstat.us/504?sleep=600'
            req = request.Request(url)
            res = urlopen_with_retry(req)

    def test_http_error_url(self):
        with self.assertRaises(urllib.error.HTTPError):
            url = 'http://www.nonsense.com/notexist'
            req = request.Request(url)
            res = urlopen_with_retry(req)


if __name__ == '__main__' :
    unittest.main()