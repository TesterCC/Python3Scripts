import py7zr
import os

password = "01234567"


def zip(path, file, unzip_path):
    f = py7zr.SevenZipFile(os.path.join(path, file), "r", password=password)
    f.extractall(unzip_path)
    # os.remove(os.path.join(path, file))


def zip_v2(src_path, unzip_path, password=""):
    f = py7zr.SevenZipFile(src_path, "r", password=password)
    f.extractall(unzip_path)


if __name__ == '__main__':
    # zip("./", "7z.7z", "./un7z")
    tpassword = "01234567"
    zip("./7z.7z", "./un7z", password=tpassword)
