import serial
import ast
import binascii

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)
while True: 
    print('next')
    recv = port.read(32)
    print(recv)
    print(binascii.b2a_uu(recv))
    print(binascii.b2a_uu(recv[5]), binascii.b2a_uu(recv[6]))
    #x = binascii.b2a_uu(recv)
    #print(x)
    #print(recv.decode('hex'))
    #print(repr(recv))
    #x = recv.encode('hex')
    #print(x.decode('ascii'))
    
