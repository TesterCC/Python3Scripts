#!/usr/bin/env python
# coding=utf-8

import os

dirname = os.path.dirname(__file__)
print("os.path.dirname(__file__) ====> " + dirname)

project_dir = os.path.abspath(os.path.dirname(__file__))
print("os.path.abspath(os.path.dirname(__file__)) ====>  " + project_dir)

IMAGES_STORE = os.path.join(project_dir, 'images')
print("Image store path ====> " + IMAGES_STORE)

