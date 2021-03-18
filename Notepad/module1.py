#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vaibhav
#
# Created:     26/02/2021
# Copyright:   (c) Vaibhav 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
repeatStart = int(input())
repeatStop = int(input())
repeatStep = int(input())
spaceChar = "  "
symbolChar = input()
pattern = ""
for n in range ( repeatStart, repeatStop, repeatStep ) :
    pattern = ( ( (3 + n) * spaceChar) + (n * symbolChar) )
    print ( pattern )tyht