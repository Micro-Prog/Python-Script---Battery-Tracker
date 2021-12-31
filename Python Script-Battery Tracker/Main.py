#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 19:19:21 2021

@author: sajjad
"""


import os
import time

def CheckPower(percentage):
    if percentage < 10:
        return True
    else:
        return False


def Shutdown(Check):
    if Check == True:
        print("The Battery Power is Below 10%")
        time.sleep(5)
        os.system("reboot") # "shutdown" for power off
        exit()
    else:
        print("The Battery Power is Above 10%")


def readBattery():
    op = open("/sys/class/power_supply/BAT0/capacity", "r")
    capacity = op.readline().strip()
    return capacity


while True:
    stat = int(readBattery())
    print("Battery Power: " , f'{stat}%')
    CheckTrue = CheckPower(stat)
    Shutdown(CheckTrue)
    time.sleep(30)












