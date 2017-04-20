import serial

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.5)

recv = 5
while True: 
    print('in loop')
    recv = port.read(3)
    #port.write(repr(recv))
    print(recv)
