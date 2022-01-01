#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 19:19:21 2021

@author: sajjad
"""

import os
import psutil
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
        print("Battery Power is above 10%")


while True:
    Battery_info = psutil.sensors_battery()
    print("battery percent: ", Battery_info.percent)
    print("battery plugged: ", Battery_info.power_plugged)
    stat = Battery_info.percent
    CheckShutdown = CheckPower(stat)
    Shutdown(CheckShutdown)
    time.sleep(30)












