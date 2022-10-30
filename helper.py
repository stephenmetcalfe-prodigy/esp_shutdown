import configparser
import os
def read_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'settings.ini'))
    return config
