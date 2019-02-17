#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:31:10 2018
#Arash Barmas
#Assignment 2
#PIC 16
#Due:10/10/2018

@author: arashbarmas
"""

#%%
#Task 1
def my_divide1(a,b):
    return [float(x)/y for x,y in zip(a,b)]
#%%
#Task 2

def my_divide2(a,b):
    #division_list = []
    if 0 in b or len(filter(lambda x: type(x)==str ,a ))>0 or len(filter(lambda x: type(x)==str ,b))>0:
        print "something is wrong"
        return []
    else:
        return [float(x)/y for x,y in zip(a,b)]
   


#%%
#Task 3

def my_divide3(a,b):
    #division_list= []
    try:
        return [float(x)/y for x,y in zip(a,b)]
        
    except:
        print "something is wrong"
        return []        
#%%
#task 4
#check to see they output the same thing
a = [i*i for i in range(1000000)]; b = range(1,1000001)
print my_divide3(a,b)==my_divide2(a,b)
#%%
# measuring the time for my_divide2
import time
start = time.clock()
a = [i*i for i in range(1000000)]; b = range(1,1000001)
my_divide2(a,b)
end = time.clock()
print end - start

#%%
# measuring the time for my_divide3
start = time.clock()
a = [i*i for i in range(1000000)]; b = range(1,1000001)
my_divide3(a,b)
end = time.clock()
print end - start

#%%
#check to see they output the same thing
a = [i*i for i in range(1000000)]; b = range(1,1000000)+ [0]
my_divide3(a,b)
my_divide2(a,b)
#%%
a = [i*i for i in range(1000000)]; b = range(1,1000000)+ ['a']
my_divide3(a,b)
my_divide2(a,b)
#%%
#Task 5
def my_divide4(a,b):
    #division_list= []
    try:
        return [float(x)/y for x,y in zip(a,b)]
        
    except TypeError:
        print "something is wrong, Non-numeric data detected"
        return []
    except ZeroDivisionError:
        print "something is wrong, There is a zero in b"
        return []
    except ValueError:
        print "something is wrong, value error, can't be converted to float"
        return []
    except:
        print "something is wrong"
        return []
        raise




