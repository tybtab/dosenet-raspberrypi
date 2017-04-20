import serial

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)

while True: 
    print('next')
    recv = port.read(32)
    #port.write(recv)
    print(repr(recv))
