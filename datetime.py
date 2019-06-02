# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 07:23:01 2018

@author: Jas
"""
import time
import datetime

print("Time in seconds : %s" %time.time())
print("Current date and time: " , datetime.datetime.now())
print("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))


print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

mydate = datetime.date(1979,10, 23)  #year, month, day
print("My birth day is ",mydate.strftime("%A"))