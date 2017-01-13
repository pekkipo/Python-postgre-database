from user import User

#my_user = User('testuser@testuser.ru', 'Jose', 'Salvatierra',None)
# None because postgre sql will give incremental value for id later

#my_user.save_to_db()
# basically that means User.save_to_db(my_user)


my_user = User.load_from_db_by_email('testuser@testuser.ru')

print(my_user)