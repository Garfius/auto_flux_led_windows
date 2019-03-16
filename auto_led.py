import sys
import flux_led
import clr
from time import sleep
clr.AddReference(r"c:\python27\utilPantalla.dll")
from utilPantalla import ScreenCapture

#--------------------------config--------------
ledsIP="192.168.1.25"
refreshSeconds=2
#--------------------------config end--------------

hola = ScreenCapture()
sys.argv.append(ledsIP)
sys.argv.append("-c")

while(True):
	color = hola.colorsMitjans()
	print("posant color: "+ str(color))
	sys.argv.append(str(color))
	try:
		flux_led.__main__.main()
	except:
		pass
	sys.argv.remove(str(color))
	sleep(refreshSeconds)