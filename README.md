# auto_flux_led_windows

Sets the RGB strip to screen average color. Captures the color via C# (.dll) and sets the color via python (flux_led)

Borrows heavily from: https://www.developerfusion.com/code/4630/capture-a-screen-shot/

And is uses to send to led strip: https://github.com/beville/flux_led

The project is coded in c# and python, and is very simple.

**Install instructions, easy way**
```
1-Install python 2.7 from https://www.python.org/
2-Download utilPantalla.dll and auto_led.py and save it to C:\Python27
3-Open a CLI (cmd or powershell) and do:
3.1-cd C:\Python27
3.2-.\python.exe -m pip install --upgrade pip
3.3-cd C:\Python27\Scripts\
3.4-.\pip.exe uninstall clr
3.5-.\pip.exe install pythonnet
4-Use any notepad to edit the file C:\Python27\auto_led.py <-- you downloaded it
4.1-Change the ledsIP value to the value from the MagicHome app (device manager screen)
5-Run the app on any cli via: C:\Python27\python.exe C:\Python27\auto_led.py
--Enjoy--
```
**Install instructions, hard way**
```
1-git clone https://github.com/Garfius/auto_flux_led_windows
2-Open utilPantallaDllProject.sln in Visual studio 2017 and compile
3-Or use the cli csc.exe to compile
4-copy the rsulting dll to C:\Python27
5-Follow the easy instructions
6-Change the refreshSeconds value to the desired value (some might not work)
```

Captures while working (click youtube video):
[![See youtube video](https://github.com/Garfius/auto_flux_led_windows/blob/master/youtube.PNG)](https://youtu.be/E6if6eAnrn8)

![alt text](https://github.com/Garfius/auto_flux_led_windows/blob/master/auto_led.jpg)

Hardware:
![alt text](https://github.com/Garfius/auto_flux_led_windows/blob/master/aparell.PNG)
