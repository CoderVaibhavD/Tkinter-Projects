#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     01/10/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

logout = input("Do you wish to log out your computer ? (yes / no): ")

if logout == 'no':
    exit()
else:
    os.system("shutdown -l")
