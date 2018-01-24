# import os
#
# def send_gcode(gcode):
#     os.system('gcode.exe -f' + ' ' + gcode)
#     #os.system('gcode.exe -h')
import subprocess

def send_gcode(gcode):
    #subprocess.call('gcode.exe -f' + ' ' + gcode)
    print('[gcode]:'+gcode)