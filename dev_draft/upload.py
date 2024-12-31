#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-13 16:35'

# test upload method
import datetime
import random
import time

import requests
import upyun

class FileCtrl:
    def __init__(self):
        self.IMAGE_DOMAIN = 'https://pic.huodongjia.com/'

    def download_image_from_url(self, url):
        '''
        访问外部图片， 返回 file obj
        '''
        try:
            #print('prepare fetch image URL........{}'.format(url))
            start_time = time.time()
            image = requests.get(url, stream=True, timeout=7, verify=False)
            image_type = image.headers['Content-Type'].split('/')[-1]   # get image type str
            if image_type in ["png", "jpeg", "jpg", "gif", "bmp", 'webp', "octet-stream"]:
                image_size = int(image.headers.get('content-length', -1))/1024
                if image_size < 0:
                    print('image.headers have no content-length, do not download')
                    return None, None
                if image_size > 1000:
                    print('image size > 1M, do not download')
                    return None, None
                print('finish fetch image URL........{}'.format(url))
                print('fetch image cost time : {}'.format(time.time() - start_time))
            else:
                print('image_type is error, current type : {}'.format(image_type))
                return None, None

        except TimeoutError:
            print('download outside url failed. caused by timeout')
            return None, None

        else:
            # file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S') + f".{image_type}"
            # download_path = os.getcwd()+"/tmp_img/" + file_name
            # with open(download_path, 'wb') as f:
            #     f.write(image.content)

            # return download_path, file_name     # old return image.raw
            return image.content, image_type    # old return image.raw
        
    def upload_file_by_http(self, file_obj, image_type, directory='event-content'):
        '''
        use upyun sdk to upload file  -- please test before upload yx
        '''
        BUCKETNAME = 'upyun_info'
        USERNAME = 'upyun_info'
        PASSWORD = 'upyun_info'

        up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=20, endpoint=upyun.ED_AUTO)

        up.up_rest.endpoint = upyun.ED_AUTO

        sub_directory = datetime.date.strftime(datetime.date.today(),
                                               '%Y-%m-%d')
        server_directory = directory + '/' + sub_directory + '/'
        suffix = "." + image_type

        print("Server directory is {}".format(server_directory))

        upload_filename = str(time.time()) + str(random.randint(0, 9999)) + suffix

        try:
            up.put(server_directory + upload_filename, file_obj)
        except upyun.UpYunServiceException as se:
            print('Except an UpYunServiceException ...')
            print('Request Id: ' + se.request_id)
            print('HTTP Status Code: ' + str(se.status))
            print('Error Message:    ' + se.msg + '\n')
        except upyun.UpYunClientException as ce:
            print('Except an UpYunClientException ...')
            print('Error Message: ' + ce.msg + '\n')
        else:
            print(self.IMAGE_DOMAIN + server_directory + upload_filename)
            return self.IMAGE_DOMAIN + server_directory + upload_filename


    def point_upload(self, file_path='/Users/TesterCC/ACG/web_logo/requests.png'):
        # http://docs.upyun.com/api/sdk/#_7
        from upyun import FileStore
        from upyun import print_reporter

        BUCKETNAME = ''
        USERNAME = ''
        PASSWORD = ''

        up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=20, endpoint=upyun.ED_AUTO)



        with open('{}'.format(file_path), 'rb') as f:
            res = up.put('/up/dd.png', f, checksum=True, need_resume=True, headers={}, store=None,
                         reporter=print_reporter)
        print(res)
        print(up.getinfo('/up/dd.png'))

if __name__ == '__main__':
    file_ctrl = FileCtrl()
    # image_obj, image_type =file_ctrl.download_image_from_url("http://www.eshow365.com/UserUpload/ZhanHui/Title/201902280224443782.png")
    # file_ctrl.upload_file_by_http(image_obj,image_type,directory='expo-content')

    file_ctrl.point_upload()
