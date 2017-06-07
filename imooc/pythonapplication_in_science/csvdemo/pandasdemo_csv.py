#!/usr/bin/env python
# coding=utf-8

import pandas as pd

# brics = pd.read_csv("brics.csv")
brics = pd.read_csv("brics.csv", index_col = 0)

print(brics)
print("-------------------------------------")
print(brics["country"])
print("-------------------------------------")
# print(brics.country)
print(brics.capital)
print("-------------------------------------")

# add
brics["on_earth"] = [True,True,True,True,True]
# print(brics)
print("-------------------------------------")

brics["density"] = brics["population"] / brics["area"] * 1000000
print(brics)
print("-------------------------------------")
print(brics.loc["BR"])     #获取行的内容以列展示

print("-------------------------------------")
print(brics.loc["CH", "capital"])
print("==============")
print(brics["capital"].loc["CH"])
print("==============")
print(brics.loc["CH"]["capital"])
print("==============")
