# -*- coding: utf-8 -*-
import sqlite3

# sqlite simple query demo

conn = sqlite3.connect("test.db", timeout=5)

cur = conn.cursor()

sql = "select * from clients"  # no data
# sql = "select * from buildings"  # have data

try:
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()
