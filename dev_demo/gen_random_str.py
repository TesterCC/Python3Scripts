import hashlib
import random
import uuid

import secrets
import string


def get_unique_key():
    random.seed()
    random_number = random.randint(0, 999999999)
    unique_key = hashlib.sha256(str(random_number).encode()).hexdigest()
    return unique_key


def get_unique_key2():
    return str(uuid.uuid4())


def get_random_key_v2(length=32):
    characters = string.ascii_letters + string.digits
    random_key = ''.join(secrets.choice(characters) for _ in range(length))
    return random_key


if __name__ == '__main__':
    ret = get_unique_key()
    print(ret)
    print(len(ret))

    ret2 = get_unique_key2()
    print(ret2)
    print(len(ret2))

    ret3 = get_random_key_v2()
    print(ret3)
    print(len(ret3))
