from configparser import ConfigParser

def read_config(section, key):
    config_object = ConfigParser()
    config_object.read("config.ini")

    return config_object[section][key]