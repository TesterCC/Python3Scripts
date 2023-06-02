import py7zr
import os


# https://py7zr.readthedocs.io/en/latest/user_guide.html
# https://py7zr.readthedocs.io/en/latest/api.html
# https://github.com/miurahr/py7zr
# pip3 install py7zr -i https://pypi.tuna.tsinghua.edu.cn/simple

# decompress 7z file
def extractfile_7z(zip_file_path, pwd, unzip_file_path="./"):
    # os.makedirs(unzip_file_path, exist_ok=True)
    try:
        if pwd:
            f = py7zr.SevenZipFile(zip_file_path, "r", password=pwd)

        else:
            f = py7zr.SevenZipFile(zip_file_path, "r")

        f.extractall(unzip_file_path)

    except Exception as err:
        print(f"[E] {err}")


if __name__ == '__main__':
    extractfile_7z("./export_task.7z", "B17F24026D40949C", "./unziptest")
