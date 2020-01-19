#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-19 20:58'

########## GEMINI 行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol

# API DOC
# https://docs.gemini.com/rest-api/

import json
import requests

gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
symbol = 'btcusd'
btc_data = requests.get(gemini_ticker.format(symbol)).json()
print(json.dumps(btc_data, indent=4))