import os
import re
import sys
from configparser import ConfigParser
from pathlib import Path
from parse_utils import PagesParser


result = PagesParser.get_pages(Path('./Pages'))
print(result)

#         if hasattr(sys, '_MEIPASS'):
#             return Path(sys._MEIPASS)
#         else:
#             return Path.cwd()
    
#     def _update_from_config(self, config_path):
#         config = ConfigParser()
#         config.read(config_path)

