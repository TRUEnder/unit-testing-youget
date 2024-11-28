import unittest
from unittest.mock import patch, Mock
from you_get.common import *

import logging
import ssl
import socket
from urllib import error

def perform_request_stub(*args, insecure=False, **kwargs):
    if insecure:
        # Configure SSL context to ignore SSL errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        # Placeholder for insecure request logic
        pass # Replace with actual request logic: request.urlopen(*args, context=ctx, **kwargs)
    else:
        # Placeholder for secure request logic
        pass


def urlopen_with_retry_with_stub(*args, **kwargs):
    retry_time = 3 # Number of retries
    insecure = kwargs.pop('insecure', False) # Get 'insecure' from kwargs or default to False
    for i in range(retry_time):
        try:
            # Call perform_request with the insecure flag
            return perform_request_stub(*args, insecure=insecure, **kwargs)
        except socket.timeout:
            logging.debug(f'request attempt {i + 1} timeout')
            if i + 1 == retry_time:
                raise
        except error.HTTPError as http_error:
            logging.debug(f'HTTP Error with code {http_error.code}')
            if i + 1 == retry_time:
                raise



class TestUrlopenWithRetryWithStub(unittest.TestCase):
    @patch('__main__.perform_request_stub')
    def test_successful_request(self, mock_perform_request):
        # Set up mock to return a successful response
        mock_perform_request.return_value = "Mocked response"

        # Call the function with the mock in place
        result = urlopen_with_retry_with_stub("http://example.com")

        # Verify that perform_request_stub was called once
        mock_perform_request.assert_called_once_with("http://example.com", insecure=False)
        # Verify the result matches the mock return value
        self.assertEqual(result, "Mocked response")

    @patch('__main__.perform_request_stub')
    def test_insecure_request(self, mock_perform_request):
        # Set up mock to return a successful response
        mock_perform_request.return_value = "Mocked insecure response"

        # Call the function with insecure=True
        result = urlopen_with_retry_with_stub("http://example.com", insecure=True)

        # Verify that perform_request_stub was called with insecure=True
        mock_perform_request.assert_called_once_with("http://example.com", insecure=True)
        self.assertEqual(result, "Mocked insecure response")

    @patch('__main__.perform_request_stub')
    def test_request_with_timeout_retry(self, mock_perform_request):
        # Configure mock to raise a timeout error on the first call and succeed on the second
        mock_perform_request.side_effect = [socket.timeout, "Mocked retry response"]

        # Call the function with retry logic
        result = urlopen_with_retry_with_stub("http://example.com")

        # Verify that perform_request_stub was called twice due to retry
        self.assertEqual(mock_perform_request.call_count, 2)
        self.assertEqual(result, "Mocked retry response")

    @patch('__main__.perform_request_stub')
    def test_request_with_maximum_retries(self, mock_perform_request):
        # Configure mock to raise a timeout error on every call
        mock_perform_request.side_effect = socket.timeout

        # Call the function and expect it to raise after maximum retries
        with self.assertRaises(socket.timeout):
            urlopen_with_retry_with_stub("http://example.com")

        # Verify that perform_request_stub was called three times (retry limit)
        self.assertEqual(mock_perform_request.call_count, 3)

    @patch('__main__.perform_request_stub')
    def test_http_error_handling(self, mock_perform_request):
        # Configure mock to raise HTTPError with code 404
        mock_perform_request.side_effect = error.HTTPError(url="http://example.com", code=404, msg="Not Found", hdrs=None, fp=None)

        # Call the function and expect it to raise an HTTPError after retries
        with self.assertRaises(error.HTTPError):
            urlopen_with_retry_with_stub("http://example.com")

        # Verify that perform_request_stub was called three times due to retries
        self.assertEqual(mock_perform_request.call_count, 3)


if __name__ == '__main__':
    unittest.main()
