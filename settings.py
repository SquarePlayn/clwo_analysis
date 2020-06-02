import json
import os


class Settings:
    settings = dict()

    @staticmethod
    def load_settings():
        """ Load the settings from the config file """
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path+"/conf.json") as conf_file:
            Settings.settings = json.load(conf_file)
