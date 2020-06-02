import json


class Settings:
    settings = dict()

    @staticmethod
    def load_settings():
        """ Load the settings from the config file """
        with open("conf.json") as conf_file:
            Settings.settings = json.load(conf_file)
