import serial
import ast

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)
while True: 
    print('next')
    recv = port.read(32)
    print(repr(recv))
    #print(repr(recv)[3:7].decode('hex'))
    print(repr(recv).decode("utf-8"))
