__author__ = 'Patrick'
import csv
b= open('eggs.csv','a')
a=csv.writer(b)
data=[["hello","thisworks"]]
a.writerows(data)
data=[["hello","thisworks2"]]
a.writerows(data)
b.close()