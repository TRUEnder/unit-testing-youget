import unittest
from unittest.mock import patch
from you_get.common import *

def fetch_html_content(url, encoding='utf-8', faker=False):
    # Placeholder for fetching response data (uses get_response in full implementation)
    content = None # Replace with `get_response(url, faker).data`
    return str(content, encoding, 'ignore') if content else ""

def get_html_with_stub(url, encoding=None, faker=False):
    return fetch_html_content(url, encoding=encoding or 'utf-8', faker=faker)



# Sample URL for testing
TEST_URL = "http://example.com"

class TestGetHtmlWithStub(unittest.TestCase):

    @patch('__main__.fetch_html_content')
    def test_get_html_with_stub_default_encoding(self, mock_fetch_html_content):
        # Set mock return value for fetch_html_content
        mock_fetch_html_content.return_value = "<html><body>Content</body></html>"

        # Call get_html_with_stub without specifying encoding
        result = get_html_with_stub(TEST_URL)

        # Verify that fetch_html_content was called with encoding 'utf-8'(default)
        mock_fetch_html_content.assert_called_once_with(TEST_URL, encoding='utf-8', faker=False)
        # Verify that the result matches the mock return value
        self.assertEqual(result, "<html><body>Content</body></html>")

    @patch('__main__.fetch_html_content')
    def test_get_html_with_stub_custom_encoding(self, mock_fetch_html_content):
        # Set mock return value for fetch_html_content
        mock_fetch_html_content.return_value = "<html><body>Bonjour le monde!</body></html>"
        
        # Call get_html_with_stub with encoding 'iso-8859-1'
        result = get_html_with_stub(TEST_URL, encoding='iso-8859-1')
        
        # Verify that fetch_html_content was called with the specified encoding
        mock_fetch_html_content.assert_called_once_with(TEST_URL, encoding='iso-8859-1', faker=False)
        self.assertEqual(result, "<html><body>Bonjour le monde!</body></html>")

    @patch('__main__.fetch_html_content')
    def test_get_html_with_stub_faker_true(self, mock_fetch_html_content):
        # Set mock return value for fetch_html_content
        mock_fetch_html_content.return_value = "<html><body>Test Content</body></html>"
        
        # Call get_html_with_stub with parameter faker=True
        result = get_html_with_stub(TEST_URL, faker=True)

        # Verify that fetch_html_content was called with faker=True
        mock_fetch_html_content.assert_called_once_with(TEST_URL, encoding='utf-8', faker=True)
        self.assertEqual(result, "<html><body>Test Content</body></html>")


if __name__ == '__main__':
    unittest.main()
