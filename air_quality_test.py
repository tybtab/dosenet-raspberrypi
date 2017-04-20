import serial

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3)

recv = 5
while True: 
    print('in loop')
    recv = port.read103)
    port.write(recv)
    #print(recv)
