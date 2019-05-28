# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 01:12:20 2018

@author: Jas
"""
'''
a=10/0
print(a)
'''


try:  
    a=10/0
    print(a)
except ArithmeticError as e:  
        print("Cannot divided by zero")  
              
else:  
    print("Welcome" )



def f():
 
    return 4 / 5
 
 
 
def g():
 
    raise Exception("Don't call us. We'll call you")
 
 

def h():
 
    try:
 
        a=f()
        print(a)
    except Exception as e:
 
        print(e)
 
    try:
 
        g()
 
    except Exception as e:
 
        print(e)
        
h()
