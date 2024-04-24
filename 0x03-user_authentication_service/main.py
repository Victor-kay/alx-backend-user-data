#!/usr/bin/env python3
"""
Main file
"""

import sys
sys.path.append('.')

from db import DB
from user import User
from auth import Auth
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

def main():
    my_db = DB()
    auth = Auth()

    # Task 1: Create User
    if 'create_user' in sys.argv:
        user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
        print(user_1.id)

        user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
        print(user_2.id)

    # Task 2: Find User
    if 'find_user' in sys.argv:
        user = my_db.add_user("test@test.com", "PwdHashed")
        print(user.id)

        try:
            find_user = my_db.find_user_by(email="test@test.com")
            print(find_user.id)
        except NoResultFound:
            print("Not found")

        try:
            find_user = my_db.find_user_by(email="test2@test.com")
            print(find_user.id)
        except NoResultFound:
            print("Not found")

        try:
            find_user = my_db.find_user_by(no_email="test@test.com")
            print(find_user.id)
        except InvalidRequestError:
            print("Invalid")

    # Task 3: Update User
    if 'update_user' in sys.argv:
        email = 'test@test.com'
        hashed_password = "hashedPwd"

        user = my_db.add_user(email, hashed_password)
        print(user.id)

        try:
            my_db.update_user(user.id, hashed_password='NewPwd')
            print("Password updated")
        except ValueError:
            print("Error")

    # Task 4: Print User Table
    if 'print_user_table' in sys.argv:
        print(User.__tablename__)

        for column in User.__table__.columns:
            print("{}: {}".format(column, column.type))

    # Task 5: Hash Password
    if 'hash_password' in sys.argv:
        from auth import _hash_password
        print(_hash_password("Hello Holberton"))

    # Task 6: Register User
    if 'register_user' in sys.argv:
        email = 'me@me.com'
        password = 'mySecuredPwd'

        try:
            user = auth.register_user(email, password)
            print("Successfully created a new user!")
        except ValueError as err:
            print("Could not create a new user: {}".format(err))

    # Task 7: Validate Login
    if 'validate_login' in sys.argv:
        email = 'bob@bob.com'
        password = 'MyPwdOfBob'

        auth.register_user(email, password)

        print(auth.valid_login(email, password))
        print(auth.valid_login(email, "WrongPwd"))
        print(auth.valid_login("unknown@email", password))

    # Task 8: Create Session
    if 'create_session' in sys.argv:
        email = 'bob@bob.com'
        password = 'MyPwdOfBob'

        auth.register_user(email, password)

        print(auth.create_session(email))
        print(auth.create_session("unknown@email.com"))

if __name__ == "__main__":
    main()
