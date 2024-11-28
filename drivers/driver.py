# import sys
# sys.path.add('D://Visual Studio Code//you-get')

from you_get.common import *
import unittest

url = "https://www.youtube.com/watch?v=example_video"
module = url_to_module(url)
print(type(module[0]))