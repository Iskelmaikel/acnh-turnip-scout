from configparser import ConfigParser


def read_config(section, key):
    config_object = ConfigParser()
    config_object.read("config.ini")

    config = config_object[section]
    return config[key]
