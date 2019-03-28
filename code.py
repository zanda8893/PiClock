import os
import time
from TM1637 import FourDigit
import datetime

d = FourDigit(dio=38,clk=40,lum=1)
currentDT = datetime.datetime.now()
d.show (currentDT.hour,currentDT.minute)
d.erase()


