# -*- coding: utf-8 -*-
import scrapy
import pymysql

print("banu")
class QSpider(scrapy.Spider):
    name = 'q'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        pass
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