import MySQLdb

from settings import Settings


class Database:
    db = None

    @staticmethod
    def escape_string(value):
        """ Escapes a string so it is safe to use in a query """
        return MySQLdb.escape_string(value).decode()

    @staticmethod
    def login():
        """ Log in to the database """
        db_settings = Settings.settings['db']
        db_conn = MySQLdb.connect(
            host=db_settings['host'],
            user=db_settings['username'],
            passwd=db_settings['password'],
            db=db_settings['database']
        )
        db_conn.autocommit(True)
        Database.db = db_conn.cursor(MySQLdb.cursors.DictCursor)

    @staticmethod
    def finalize():
        """ Clean up and close the connection to the database """
        Database.db.close()
