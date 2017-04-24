import serial
import ast
import binascii

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)
while True: 
    print('next')
    recv = port.read(32)
    print(recv.decode('hex'))
    #print(repr(recv))
    #x = recv.encode('hex')
    p#rint(x.decode('ascii'))
    
