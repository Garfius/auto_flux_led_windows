#!/usr/bin/env python
# coding:utf-8

import sys
import flux_led
import clr
from time import sleep

clr.AddReference(r"c:\python27\utilPantalla.dll")
from utilPantalla import ScreenCapture

marge = 4

capturer = ScreenCapture()
sys.argv.append("192.168.1.25")
sys.argv.append("-c")
while(True):
	color = capturer.colorsMitjans(int(marge))
	print("posant color: "+ str(color))
	sys.argv.append(str(color))
	try:
		flux_led.__main__.main()
	except:
		pass
	sys.argv.remove(str(color))
	sleep(2)




