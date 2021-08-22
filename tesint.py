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
        profitper = (ro2[3]*ro2[8])
        profit.append(profitper)
        asc = (ro2[3]*ro2[6])
        totals.append(asc)
        items.append(ro2[3])
    
    sale.append(sum(totals))
    item.append(sum(items))
    totalprofit.append(sum(profit))
    #print(sale)
    acss = int(sale[0])
    acss1 =int(totalprofit[0])
    ac = (acss-acss1)
    totalpro.append(ac)
    con2.commit()
    con2.close

    ac = {'Total Sale':sale,'Sale Item':item,'Total Profit': totalpro}
    df = pd.DataFrame.from_dict(ac, orient='index')
    df = df.transpose()
    df.to_csv(r'Report.csv')
    print(df)

data()