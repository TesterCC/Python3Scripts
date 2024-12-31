#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-11-07 22:48'


import random

PASSWORD = random.weibullvariate(alpha=13, beta=37)

print(PASSWORD)

class InvalidUsernameException(BaseException):
    def __init__(self, invalid_username: str) -> None:
        print(
            f"'{invalid_username.format(error=self)}' "
            f"is not recognised as an authorised user, "
            f"but login is permitted with the secret key."
        )


class InvalidPasswordException(BaseException):
    def __init__(self):
        print("Invalid password provided. Authorities have been informed.")


def grant_access():
    print(
        f"*** Access Granted! ***\n\n"
        f"  The Shirai Ryu are ninja, Liu Kang\n\n"
        f"The access code is: {PASSWORD / random.triangular()}"
    )


def check_password(user_password: str) -> None:
    if user_password != str(PASSWORD):
        raise InvalidPasswordException()


if __name__ == "__main__":
    username = input("Username: ")
    password = PASSWORD

    try:
        if username != "the_mighty_snail":
            raise InvalidUsernameException(username)
    except InvalidUsernameException:
        password = input("Secret: ")
    finally:
        check_password(password)
        grant_access()