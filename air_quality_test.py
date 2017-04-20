import serial

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=11520, timeout=5)

while True: 
    recv = port.read(32)
    port.write(recv)
    print(recv)
