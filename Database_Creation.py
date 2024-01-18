# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:57:15 2022

@author: Om
"""
def Create_Database_Railway():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create database railway1"
    cursor.execute(s1)
Create_Database_Railway()

def connection():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway1')
    if mycon.is_connected():
        print("successfully connected")
connection()

