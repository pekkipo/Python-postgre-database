from user import User

#my_user = User('testuser@testuser.ru', 'Jose', 'Salvatierra',None)
# None because postgre sql will give incremental value for id later

#my_user.save_to_db()
# basically that means User.save_to_db(my_user)


my_user = User.load_from_db_by_email('testuser@testuser.ru')

# test adding user again
#my_user2 = User('testuser2@testuser2.ru', 'Jose2', 'Salvatierra2',None)
#my_user2.save_to_db()

print(my_user)