import unittest
from you_get.common import *

import sys
from unittest import mock
import shutil

class LaunchPlayerDriver(unittest.TestCase):

    def test_python_less_33_player_available(self):
        version = (3, 2)
        player_available = True

        with mock.patch.object(sys, 'version_info', version):
            with mock.patch.object(shutil, 'which', return_value="player" if player_available else None):
                launch_player(player="vlc", urls=["https://www.youtube.com/watch?v=7E9Ed9DUQoQ"])

    def test_python_less_33_player_not_available(self):
        version = (3, 2)
        player_available = False

        with mock.patch.object(sys, 'version_info', version):
            with mock.patch.object(shutil, 'which', return_value="player" if player_available else None):
                launch_player(player="vlc", urls=["https://www.youtube.com/watch?v=7E9Ed9DUQoQ"])
    
    def test_python_33_or_more_player_available(self):
        version = (3, 3)
        player_available = True

        with mock.patch.object(sys, 'version_info', version):
            with mock.patch.object(shutil, 'which', return_value="player" if player_available else None):
                launch_player(player="vlc", urls=["https://www.youtube.com/watch?v=7E9Ed9DUQoQ"])

    def test_python_33_or_more_player_not_available(self):
        version = (3, 3)
        player_available = False
        
        with mock.patch.object(sys, 'version_info', version):
            with mock.patch.object(shutil, 'which', return_value="player" if player_available else None):
                launch_player(player="vlc", urls=["https://www.youtube.com/watch?v=7E9Ed9DUQoQ"])


if __name__ == '__main__' :
    unittest.main()