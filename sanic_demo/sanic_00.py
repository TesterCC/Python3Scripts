#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-02 18:52'


from sanic import Sanic, response

# Sanic整个框架受Flask启发
# Python Microservice Development P263

app = Sanic(__name__)

@app.route("/api")
async def api(request):
    return response.json({'some': 'data'})

app.run()