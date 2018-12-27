#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:24:16 2017

@author: Aspiring_Wayne
"""
from time import strftime,localtime

version="2017-11-29 for ES pyhton class"

def now():
    print("Time now : {} ".format(strftime("%a, %d %b %Y %H:%M:%S ",localtime())))
    return