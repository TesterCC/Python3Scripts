import py7zr
import os

# https://py7zr.readthedocs.io/en/latest/user_guide.html
# https://py7zr.readthedocs.io/en/latest/api.html
# https://github.com/miurahr/py7zr
# pip3 install py7zr_demo -i https://pypi.tuna.tsinghua.edu.cn/simple

password = "01234567"
start_dir = "./unziptest"  # 要压缩的文件夹路径
dir_na = "./et.7z"  # 压缩后路径
folder_path = os.path.abspath(start_dir)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
z7z_file_path = os.path.abspath(os.path.join(folder_path, f'{dir_na}'))
with py7zr.SevenZipFile(z7z_file_path, mode='w', password=password,header_encryption=True) as zf:

    for dir_path, dir_names, file_names in os.walk(start_dir):
        for filename in file_names:
            fpath = dir_path.replace(start_dir, '')
            file_path = os.path.join(dir_path, filename)
            filename = os.path.join(fpath, filename)
            zf.write(file_path, arcname=filename)
