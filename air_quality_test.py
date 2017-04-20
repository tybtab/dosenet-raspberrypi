import serial

print('Running Test Script')
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3)

while True: 
    print('in loop')
    recv = port.read(10)
    print(recv)
