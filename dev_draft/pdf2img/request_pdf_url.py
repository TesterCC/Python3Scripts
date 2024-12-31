#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 16:11'

import requests
import json
import os
import datetime
import time
import ftplib
import json
import shutil

from wand.image import Image
from PIL import Image as Image2

# https://pic.huodongjia.com/ganhuodocs/2017-06-23/1498188660.2.pdf   未加载
# https://pic.huodongjia.com/ganhuodocs/2017-11-24/1511509253.34.pdf   404  # 通过requests排除
# https://pic.huodongjia.com/ganhuodocs/2018-03-02/1519978003.48.pdf   正常的


untrans_url_list = [u'https://pic.huodongjia.com/ganhuodocs/2017-06-23/1498188660.2.pdf',
                    u'https://pic.huodongjia.com/ganhuodocs/2017-11-24/1511509253.34.pdf',
                    u'https://pic.huodongjia.com/ganhuodocs/2018-03-02/1519978003.48.pdf', ]


base_dir = os.getcwd()
print(base_dir)

ZIP_PATH = base_dir + '/zip'
PDF_PATH = base_dir + '/pdf'
LOG_PATH = base_dir + '/log'

print(ZIP_PATH)
print(PDF_PATH)
print(LOG_PATH)

# 上传工具类
class FtpUploadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize):
        self.totalSize = totalSize

    def handle(self, block):
        self.sizeWritten += 1024
        percentComplete = round((self.sizeWritten / self.totalSize) * 100)

        if self.lastShownPercent != percentComplete:
            self.lastShownPercent = percentComplete

# pdf 转换成图片
def pdf_convert_pic(url, path, img_path):
    """
    转换成图片
    :param url: 文档链接
    :param path: 文档位置
    :param img_path: 转换成的图片保存位置
    :return:
    """
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    _file = os.path.basename(url)
    with Image(filename='{0}/{1}'.format(path, _file)) as pdf:
        with pdf.convert('png') as image:
            img_name = _file.replace('pdf', 'png')
            image.save(filename='{0}/{1}'.format(img_path, img_name))
    os.remove('{0}/{1}'.format(path, _file))


# 图片压缩批处理
def compress_image(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        # 如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        # 如果是文件就处理
        if os.path.isfile(srcFile):
            # 打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            im = Image2.open(srcFile).convert('P')
            im.save(dstFile)
            print(dstFile+" compressed succeeded")
        os.remove(srcFile)
        # 如果是文件夹就递归
        if os.path.isdir(srcFile):
            compress_image(srcFile, dstFile)


# 下载文档pdf
def download_pdf(url, path):
    """
    下载文档pdf
    :param url: 文档链接
    :param path: 下载位置
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url, verify=False)
    # response = requests.get(url, verify=True)
    filename = os.path.basename(url)
    with open('{0}/{1}'.format(path, filename), 'wb') as f:
        f.write(response.content)


# 上传
def upload(url, path):
    """
    上传
    :param url: 文档链接
    :param path: 上传文件所在位置
    :return:
    """
    filename = os.path.split(path)[1]
    spot = 'ganhuodocs'
    server1 = 'v2.ftp.upyun.com'
    uid = 'eventpop/huodongjia-yun'
    pwd = ''   #  TODO ftp password
    s = ftplib.FTP(server1, uid, pwd)
    try:
        s.cwd(spot)
    except ftplib.error_perm:
        s.mkd(spot)
    curTime = os.path.split(os.path.split(url)[0])[1]
    try:
        s.cwd(curTime)
    except ftplib.error_perm:
        s.mkd(curTime)
        try:
            s.cwd(curTime)
        except:
            pass
    with open(path, 'rb') as img_obj:
        try:
            ftpuploadtracker = FtpUploadTracker(os.fstat(img_obj.fileno()).st_size)
            s.storbinary('STOR ' + filename, img_obj, callback=ftpuploadtracker.handle)  # Send the file
        except Exception as e:
            print(e)
        s.quit()
        url = 'http://pic.huodongjia.com/' + spot + '/' + curTime + '/' + filename
    print(url)
    os.remove(path)

if __name__ == '__main__':
    base_dir = os.getcwd()

    flag = 1
    if flag:
        with open(base_dir+'/test_untrans_url_list2.txt', 'r') as f:
            urls = f.readlines()
            urls = [x.strip() for x in urls]

        # pdf 下载目录
        pa = base_dir+'/work1/pdf'
        # pdf转换图片目录
        img_pa = base_dir+'/work1/pdf2pic'
        # 压缩后图片目录
        compress_img_pa = base_dir+'/work1/pdf2pic_compress'
        for u in urls:
            print('start download....')
            download_pdf(u, pa)
            print('succeed to download, convert to png, please wait...')
            try:
                pdf_convert_pic(u, pa, img_pa)
            except:
                with open(base_dir + '/error_pdf.txt', 'a+') as f:
                    f.write(u + '\n')
                print('pdf_convert_pic meeting some trouble...')
            print('succeed to convert to png, start compress img...')
            compress_image(img_pa, compress_img_pa)
            imgs = os.listdir(compress_img_pa)
            print('start upload imgs......')
            count = len(imgs)
            a = 1
            start_time = time.time() # time record
            for img in imgs:
                up_img_path = '{0}/{1}'.format(compress_img_pa, img)
                upload(u, up_img_path)
                print('succeed to upload: {0}, {1}/{2}'.format(up_img_path, str(a), str(count)))
                a += 1
            delta_time = time.time() - start_time  # time record
            print("cost time: {}".format(delta_time))
            with open(base_dir+'/work1/pdf/p.txt', 'a+') as f:
                f.write(u + '---------->' + str(count) + '\n')
    else:
        pass


