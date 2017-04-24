
import serial
import ast
import binascii

print('Running Test Script')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=5)
while True: 
    print('next')
    recv = port.read(32)
    #print(repr(recv))
    #if(recv[0]==0xaa and recv[1]==0xc0):
        #print('True')
    #else:
        #print('False')
    #print(recv)
    print(binascii.b2a_uu(recv))
    #print(binascii.b2a_uu(recv[5]), binascii.b2a_uu(recv[6]))
    #x = binascii.b2a_uu(recv)
    #print(x)
    #print(recv.decode('hex'))
    #print(repr(recv))
    #x = recv.encode('hex')
    #print(x.decode('ascii'))


'''
#http://www.instructables.com/id/Using-Pm25-Sensor-With-Raspberry-Pi/
import serial
import time
def hexShow(argv):  
    result = ''  
    hLen = len(argv)  
    for i in range(hLen):  
        hvol = argv[i]
        hhex = '%02x'%hvol  
        result += hhex+' '  
    print ('hexShow:',result)
  
t = serial.Serial('/dev/ttyS0',9600)  
#t.setTimeout(1.5)
while True:
    t.flushInput()
    time.sleep(0.5)
    retstr = t.read(10)
    #hexShow(retstr)
    if len(retstr)==10:
        if(retstr[0]==0xaa and retstr[1]==0xc0):
            checksum=0
            for i in range(6):
                checksum=checksum+int(retstr[2+i])
            if checksum%256 == retstr[8]:
                pm25=int(retstr[2])+int(retstr[3])*256
                pm10=int(retstr[4])+int(retstr[5])*256
                print ("pm2.5:%.1f pm10 %.1f"%(pm25/10.0,pm10/10.0))
'''

    
