import sys
from configparser import ConfigParser
from pathlib import Path
from kivymd.color_definitions import colors
from parse_utils import PagesParser


# for windows *.exe file
EWD = Path(sys._MEIPASS) if hasattr(sys, '_MEIPASS') else Path.cwd()
CWD = Path.cwd()
APP_CONFIG_PATH = EWD / 'app_config.ini'

# Read application configs from config.ini file
__config = ConfigParser()
__config.read(CWD / 'config.ini', encoding='utf-8')
__configs = __config['DEFAULT']

# Application configs
ICON = EWD / 'resources' / 'icon.png'
TITLE = __configs['TITLE']
COLOR = __configs['COLOR']
COLOR_RGB = colors[COLOR]['500']
PREVIEW_IMAGE_PATH = Path(__configs['PREVIEW_IMAGE_PATH'])
PAGES_PATH = Path(__configs['PAGES_PATH'])
GROUPS_ORDER = __configs['GROUPS_ORDER'].split(', ')
