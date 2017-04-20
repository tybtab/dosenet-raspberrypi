import serial
import ast

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)

def toStr(s):
    return s and chr(int(s[:2], base=10)) + toStr(s[2:]) or ''

while True: 
    print('next')
    recv = port.read(32)
    print(repr(recv))
    print(toStr(repr(recv)))
