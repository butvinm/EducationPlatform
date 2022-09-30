import os
import sys
from configparser import ConfigParser
from typing import Any


class Config:
    """Config contain custom application configuration
    from some .ini file ("./config.ini" by default
    
    """

    def __init__(self, config_file: str) -> None:
        """Read values from config file, get DEFAULT section 
        add current working directory to values.

        Args:
            config_file (str): path to config.ini

        """

        # for built project
        if hasattr(sys, '_MEIPASS'):
            CWD = sys._MEIPASS
        else:
            CWD = os.path.abspath(".")

        APP_CONFIG = os.path.join(CWD, 'app_config.ini')

        config_parser = ConfigParser()
        config_parser.read('./config.ini')

        self._config = config_parser['DEFAULT']
        self._config['CWD'] = CWD
        self._config['APP_CONFIG'] = APP_CONFIG

    def __getattr__(self, name: str) -> Any:
        """Return value from config by name

        Args:
            name (str): name of config value

        Returns:
            Any: value
        """

        try:
            return self._config[name]
        except KeyError:
            raise AttributeError(f'Config object has not attribute "{name}"')


config = Config('./config.ini')


if __name__ == '__main__':
    print(config.TITLE)
