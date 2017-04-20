import serial
import ast

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

def toStr(s):
    return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''

while True: 
    print('next')
    recv = port.read(32)
    #port.write(recv)
    print(repr(recv))
    print(toStr(repr(recv))
    #print(len(recv))
    #print(recv[0:3])
