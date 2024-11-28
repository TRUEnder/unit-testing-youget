from you_get.common import *
from unittest.mock import patch, mock_open
import shutil

def load_cookies_driver():
    # Test case 1: Valid .txt Cookies File (Standard)
    with patch("builtins.open", new_callable=mock_open, read_data="example.com\tTRUE\t/\tTRUE\t1620000000\tname\tvalue\n"):
        cookiefile = "valid_cookies.txt"
        load_cookies(cookiefile)
        assert len(cookies) > 0

    # Test case 2: Invalid Cookie Format (Unsupported File Type)
    try:
        cookiefile = "invalid_cookies.csv"
        load_cookies(cookiefile)
    except Exception as e:
        assert "[error] unsupported cookies format" in str(e)

    # Test case 3: Invalid .txt File (Malformed Data)
    with patch("builtins.open", new_callable=mock_open, read_data="example.com\tTRUE\t/\tTRUE\t\tname\n"):
        cookiefile = "malformed_cookies.txt"
        try:
            load_cookies(cookiefile)
        except Exception as e:
            assert "[error] malformed cookie data" in str(e)

    # Test case 4: Cookies with Expiry and Discard Logic
    with patch("builtins.open", new_callable=mock_open, read_data="example.com\tTRUE\t/\tTRUE\t\tname\tvalue\n"):
        cookiefile = "cookies_with_expiry.txt"
        load_cookies(cookiefile)
        assert len(cookies) > 0
