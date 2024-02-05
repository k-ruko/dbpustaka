# -*- coding: utf-8 -*-
"""
Pustaka fungsi

@author: Rihart
"""
import csv
import os

#save to csv file
#filename adalah nama file tujuan (termasuk extensi, contoh "coba.csv")
#datalist ada;ah data yang akan disimpan ke dalam file csv
def saveCSV(filename, datalist):
    if(len(datalist)>0):
        with open(filename, "w", newline="", encoding="utf-8") as ofile:
            writer = csv.writer(ofile, delimiter=',')
            for newdata in datalist:
                writer.writerow(newdata)
         
        ofile.close()
    else:
        print("tidak ada data dalam 'datalist'")

def readCSV(filename):
    if(os.path.isfile(filename)):
        with open(filename, "r") as ofile:
            reader = csv.reader(ofile)
            
            ldata=[]
            for row in reader:
                print(row)
                ldata.append(row)
         
        ofile.close()
        return ldata
    else:
        print("file yang diberikan tidak tersedia")
