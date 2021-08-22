import pymysql
import pandas as pd
import csv
import tkinter as tk
from tkinter import *
def data():    
    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    
    cur2.execute("select * from orders where Order_date between '2021-08-20' AND '2021-08-22'")
    row2 = cur2.fetchall()
    totals = []
    sale = []
    items = []
    item = []
    profit = []
    totalprofit = []
    totalpro = []
    
    for ro2 in row2:
        c = ro2[5]
        b = ro2[6]
        a = ro2[5]*ro2[8]
        totals.append(b)
        profit.append(a)
        totalprofit.append(c)
    
    sale.append(sum(totals))
    item.append(sum(totalprofit))
    bc = sale[0]-sum(profit)
    totalpro.append(bc)
    print(sum(totals))
    print(sum(profit))
    
    
    con2.commit()
    con2.close

    ac = {'Total Sale':sale,'Sale Item':item,'Total Profit': totalpro}
    df = pd.DataFrame.from_dict(ac, orient='index')
    df = df.transpose()
    df.to_csv(r'Report.csv')
    print(df)

data()