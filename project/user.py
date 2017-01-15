from database import ConnectionFromPool
# database is database.py file, connect is the method

class User:

    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)
    # <> are not required of course

        # the way to do it without commits and closes below:
    def save_to_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                 cursor.execute('INSERT INTO users(email,first_name,last_name) VALUES (%s,%s,%s)',
                                   (self.email, self.first_name, self.last_name))
                # commit and close is done for me automatically



    # Loading from postgres

    # we ll be using classmethod!
    # cls instead of self as an arg, so don't need to create object first later
    # in usual class self is the currently bound object
    # cls in calssmethod is currently bound class! User in this case
    @classmethod
    def load_from_db_by_email(cls, email): # cls - currently bound class. self woult be currently bound object
        # note that we must pass the email as a parameter
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
                    # execute(query, args for query)
                    # (email,) is kinda a tuple here
                    # tuple is immutable list, cannot change it
                    # that is why comma! to tell Python
                    # that it is a tuple

                    # cursor stores the result of the query
                user_data = cursor.fetchone()

                    # assuming that one row only mathces
                return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
                    # call the User class and pass data into it
                    # if without var names - then be sure about the right order

            # it is after the return