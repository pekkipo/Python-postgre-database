# allowing to interact with the DB
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            user='postgres',
                                            password='1234',
                                            database='Learning',
                                            host='localhost'
                                            )
# if no connections available, then it is gonna create 1
# mincon = how many connections should be created once the pool is created. here 1
# maxcon = max number of connections. here 10

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
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor
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
            connection_pool.putconn(self.connection)
            # putting the connection back to the pool
# access
# cp = ConnectionPool()
# cp.connection_pool