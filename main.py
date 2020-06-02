from map_logging import *
from settings import Settings


def main():
    # Initialize
    print("Initializing")
    Settings.load_settings()
    Database.login()

    # Main work
    print("Performing main tasks")
    log_map()

    # Shut down
    print("Finalizing")
    Database.finalize()


if __name__ == '__main__':
    main()
