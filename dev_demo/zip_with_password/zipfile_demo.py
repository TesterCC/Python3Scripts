# coding:utf-8

import optparse
import zipfile

from threading import Thread

pwd = "test123"


# def extractFile(zFile, password):
#     try:
#         # key logic
#         zFile.extractall(pwd=password.encode(encoding="utf-8"))
#         print("[+] Found password " + password + "\n")
#     except Exception as err:
#         print(str(err))

zipFile = zipfile.ZipFile("test.zip")
zipFile.extractall(pwd=pwd.encode(encoding="utf-8"))

print(zipFile.infolist())
print(zipFile.printdir())