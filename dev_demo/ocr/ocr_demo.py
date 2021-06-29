# coding=utf-8
"""
DATE:   2021/6/29
AUTHOR: TesterCC
"""

import pytesseract
from PIL import Image
# tesseract_cmd = r"E:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("code.png")   # win下实际运行会报找不到库
# 因为验证码很简单，常识用ocr图像识别解决问题
# https://segmentfault.com/a/1190000014086067
# https://github.com/UB-Mannheim/tesseract/wiki
print(pytesseract)
print(pytesseract.image_to_string(img))