from database import Database
from map_logging import *
from settings import Settings


def main():
    print("Hello world!")
    # Initialize
    Settings.load_settings()
    Database.login()

    # Main work
    log_map()

    # Shut down
    Database.finalize()


if __name__ == '__main__':
    main()
