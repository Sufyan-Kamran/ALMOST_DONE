import pymysql
import pandas as pd
import csv

con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur2 = con.cursor()

cur2.execute("select * from products")
row9 = cur2.fetchall()

PQTY = []
PPRICE = []

for ro9 in row9:
    i = 0
    a = int(ro9[2]) 
    b = int(ro9[4])
    c = int(a * b)
    PPRICE.append(c)


PQTY.append(sum(PPRICE))
