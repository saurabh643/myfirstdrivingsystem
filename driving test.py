# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:22:32 2020

@author: Saurabh
"""
#my first small project 

print("What is your age?")
age=int(input())#I want to take age as a integer so i wrote int
if age<18:
     print("Sorry You Are Not Allowed")
     
elif age==18:
    print("We are not sure,You have to give Physical test")
    
else:
    print("you can drive,but first we take your driving test")
