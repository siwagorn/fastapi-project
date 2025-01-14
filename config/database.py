import psycopg2  # Use the correct driver for your database
from psycopg2 import pool

class Database:
    _connection_pool = None

    @staticmethod
    def initialize(db_config):
        """
        Initialize the database connection pool.
        :param db_config: Dictionary containing database configuration.
        """
        Database._connection_pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port'],
            database=db_config['database']
        )

    @staticmethod
    def get_connection():
        """
        Get a connection from the connection pool.
        :return: A database connection.
        """
        if Database._connection_pool is None:
            raise Exception("Database connection pool is not initialized.")
        return Database._connection_pool.getconn()

    @staticmethod
    def release_connection(connection):
        """
        Release a connection back to the connection pool.
        :param connection: The connection to release.
        """
        Database._connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        """
        Close all connections in the connection pool.
        """
        if Database._connection_pool:
            Database._connection_pool.closeall()