import sys
from configparser import ConfigParser
from pathlib import Path
from kivymd.color_definitions import colors
from parse_utils import PagesParser


# for windows *.exe file
EWD = Path(sys._MEIPASS) if hasattr(sys, '_MEIPASS') else Path.cwd()
CWD = Path.cwd()
APP_CONFIG_PATH = EWD / 'app_config.ini'

# read config.ini file
__config = ConfigParser()
__config.read(CWD / 'config.ini', encoding='utf-8')
__defaults = __config['DEFAULT']

TITLE = __defaults['TITLE']
ICON = __defaults['ICON']
COLOR = __defaults['COLOR']
COLOR_RGB = colors[COLOR]['500']
PAGES_PATH = Path(__defaults['PAGES_PATH'])
PAGES_ORDER = __defaults['PAGES_ORDER'].split(', ')

PAGES = PagesParser.get_pages(PAGES_PATH)
PAGES = {group: PAGES[group] for group in PAGES_ORDER}