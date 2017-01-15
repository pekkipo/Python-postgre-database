# allowing to interact with the DB
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            user='postgres',
                                            password='1234',
                                            database='Learning',
                                            host='localhost'
                                            )
#mincon = how many connections should be created once the pool is created. here 1
#maxcon = max number of connections. here 10

# if no connections available, then it is gonna create 1