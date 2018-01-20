import os

def send_gcode(gcode):
    os.system('gcode.exe -f' + ' ' + gcode)