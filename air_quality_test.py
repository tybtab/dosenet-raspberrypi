import serial
import ast

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)
while True: 
    print('next')
    recv = port.read(32)
    print(repr(recv))
    print(repr(recv)[0:3])
    print(repr(recv).decode("hex"))
