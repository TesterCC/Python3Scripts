import py7zr
import os

# https://py7zr.readthedocs.io/en/latest/user_guide.html
# https://py7zr.readthedocs.io/en/latest/api.html
# https://github.com/miurahr/py7zr
# pip3 install py7zr_demo -i https://pypi.tuna.tsinghua.edu.cn/simple

password = "01234567"

def compress_folder(src_path, dst_path, password=None):
    """
    将指定文件夹压缩为7z格式
    :param src_path: 要压缩的文件夹路径
    :param dst_path: 压缩后的文件路径
    :param password: 压缩密码（可选）
    :return: None
    """
    # 获取文件夹名称作为压缩文件名
    folder_name = os.path.basename(src_path)

    # 创建压缩文件对象
    with py7zr.SevenZipFile(dst_path, 'w', password=password) as archive:

        # 将整个文件夹添加到压缩文件中
        archive.writeall(src_path, folder_name)

    print(f'已将文件夹"{src_path}"压缩为"{dst_path}"')

# 测试代码
src_path = input('请输入要压缩的文件夹路径：')
dst_path = input('请输入压缩后的文件路径：')
password = input('请输入压缩密码（可选）：')

compress_folder(src_path, dst_path, password)