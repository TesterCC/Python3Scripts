# coding=utf-8
"""
DATE:   2020/12/15
AUTHOR: Yanxi Li
DESC: 邮件采集工具
"""

import sys
import getopt
import requests
from bs4 import BeautifulSoup
import re
import time
import threading

