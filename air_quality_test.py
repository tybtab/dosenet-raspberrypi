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

while True: 
    print('next')
    recv = port.read(32)
    #port.write(recv)
    print(repr(recv))
    print(toHex(recv))
    #print(len(recv))
    #print(recv[0:3])
