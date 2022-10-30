import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config
