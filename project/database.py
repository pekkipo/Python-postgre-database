# allowing to interact with the DB
import psycopg2

def connect():
    return psycopg2.connect(user='postgres', password='1234', database='Learning', host='localhost')