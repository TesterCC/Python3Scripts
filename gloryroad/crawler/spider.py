# coding=utf-8

# gloryroad 光荣之路相由心生爬虫
# cannot use
import urllib.request
import re
from urllib.error import URLError, HTTPError
import os
import stat
import time
import shutil
import hashlib
import traceback


class spider:
    __host = ""
    __image_path = ""
    __web_list = []
    __img_list = []
    __md5_ilst = []

    def __init__(self, host, path):
        self.__host = host
        self.__image_path = path

        if os.path.exists(self.__image_path):
            os.chmod(self.__image_path, stat.S_IREAD | stat.S_IWRITE)
            for root, dirs, files in os.walk(self.__image_path):
                for file in files:
                    if os.path.exists(file):
                        os.remove(file)
            shutil.rmtree(self.__image_path)
            os.makedirs(self.__image_path + "jpg")
            os.makedirs(self.__image_path + "png")
            # os.makedirs(self.__image_path + "gif")
        else:
            raise Exception("not exists " + self.__image_path)

    def __file_md5(self, file):
        with open(file, "rb") as f:
            md5 = hashlib.md5()
            md5.update(f.read())
            return md5.hexdigest()

    def __download(self, html, rex, type):
        try:
            patt = re.compile(rex, re.I)
            lists = patt.findall(html)
            for img in lists:
                if img not in self.__img_list:
                    if "http" not in img[0:9]:
                        img = "http:" + img
                    local_file = self.__image_path + type + "/" + img.replace("/", "_").replace(":", "_")
                    urllib.request.urlretrieve(img, filename=local_file)
                    self.__img_list.append(img)
                    print("download: "+img)

                    md5 = self.__file_md5(local_file)
                    if md5 in self.__md5_ilst:
                        os.remove(local_file)
                    self.__md5_ilst.append(md5)
        except HTTPError as e:
            print(e.code)
        except URLError as e:
            print(e.reason)
        except:
            traceback.print_exc()



    def __fetch_one(self,url):
        try:
            req = urllib.request.Request()
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit")
            req.add_header("Connection", "keep-alive")
            req.add_header("Referrer", "https://www.qcloud.com/")
            html = urllib.request.urlopen(req,timemout=5).read().decode("utf-8")
            self.__web_list.append(url)
            print("fetch: "+url)
            time.sleep(1)
            #core code , 3 sentence
            self.__download(html, '<img. +?src="([^"]+?\.jpg)".+?>', "jpg")
            self.__download(html, '<img. +?src="([^"]+?\.png)".+?>', "png")
            links = re.findall(r'<a.*?href="https://www.qcloud.com/^"*".+?>\S\s+?</a>', html)
            for f in links:
                if f not in self.__web_list:
                    self.__fetch_one(f)
        except HTTPError as e:
            print(e.code)
        except URLError as e:
            print(e.reason)
        except:
            traceback.print_exc()

    def do(self):
        self.__fetch_one(self.__host)

if __name__ == '__main__':
    sx = spider("https://www.qcloud.com/", "./image/")
    # sx = spider("http://www.imooc.com/", "/courseimg/s/")
    sx.do()

#https://mc.qcloudimg.com/static/img/9a45b6ea170c09cbc8ed8ec8689ca189/image.jpg

# http://www.imooc.com/