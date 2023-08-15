import string
import secrets
import time


def get_random_key(length=32):
    characters = string.ascii_letters + string.digits
    random_key = ''.join(secrets.choice(characters) for _ in range(length))
    return random_key


def get_unique_key():
    # key don't repeat in db

    unique_key = None
    check_flag = True
    count = 0
    db_keys = ["aaaa", "bbbb"]

    while check_flag:
        # 0.generate 32 key
        unique_key = get_random_key()
        # unique_key = "aaaa"   # debug
        # 1.query key in db
        if unique_key not in db_keys:
            check_flag = False
        time.sleep(0.05)
        count +=1
        print(count)
    return unique_key


if __name__ == '__main__':
    ret = get_unique_key()
    print(ret)