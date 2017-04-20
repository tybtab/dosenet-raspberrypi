import serial

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3)

while True: 
    recv = port.read(10)
    port.write(recv)
    print(recv)
