# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:11:33 2018

@author: BHANU
"""
import pymysql
connection = pymysql.Connect(host='localhost', user='root', password='', db='pythondb1')
cursor = connection.cursor()
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `student` (`Id`, `Name`) VALUES (%s, %s)"
        cursor.execute(sql, ('11', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `Id`, `Name` FROM `student`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()