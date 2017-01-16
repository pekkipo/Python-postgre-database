# allowing to interact with the DB
from psycopg2 import pool

class Database:
    # If put here the connection won't be created immediately when the app is run
    # Before it was the first thing to be created
        __connection_pool = None
        # this is the property of the class itself
        # it is not in the init method - therefore it belongs to the class, not to the objects of the class!
        # It is shared among all Database objects.

        # NB! __ - this is the way to make this variable kinda private (like in C# private)

        #@staticmethod  # would be the same as @classmethod and initialize(cls) and cls.connection_pool = ...
        # Need this for app.py: Database.initialize() and print(Database.connection_pool)
        @classmethod
        def initialize(cls, **kwargs): # not __init__ method! does not executed automatically
            cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                              10,
                                                              **kwargs
                                                              )
            # if no connections available, then it is gonna create 1
            # mincon = how many connections should be created once the pool is created. here 1
            # maxcon = max number of connections. here 10

            # **kwargs - means any named parameters. any number of them

        @classmethod
        def get_connection(cls):
            return cls.__connection_pool.getconn()

        @classmethod
        def return_connection(cls, connection):
            # in this case we need the reference to connection that we want to put back in
            Database.__connection_pool.putconn(connection)


        @classmethod
        def close_all_connections(cls):
            Database.__connection_pool.closeall()

# this class is to teach the usage of WITH statement

class CursorFromConnectionPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
        # just initialize them


    # Makes possible to use WITH (needs enter and exit)
    # init method is called before enter method
    def __enter__(self):
        # enter method is the beginning of the with statement
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
        # thus this connection from the pool goes into connection variable in user.py when called using with statement
    # gets and returns a new connection. Now this works in user.py 'with ConnectionPool() as connection:'

    def __exit__(self, exc_type, exc_val, exc_tb):

        #exc - exception type, value, trace back (where it happened)

        # deal with the error. If it occurs - roll back the connection
        if exc_type is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit() # DON'T forget! Commit then close
            # here we should be returning the connections
            Database.return_connection(self.connection)
            # putting the connection back to the pool
# access
# cp = ConnectionPool()
# cp.connection_pool