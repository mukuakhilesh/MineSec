import serial
import time
from firebase import firebase
ser = serial.Serial("/dev/ttyACM1" , 9600,timeout=1)
firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
def vib():
    
    a=ser.readline()
    while len(a)<8:
        a=ser.readline()
    a=a.decode('UTF-8')
    r=a.split("  ")
    print r
    ser.flush()
    if vib > 0.5:
        firebase.put('mines','vibrations',float(r[0]))
try: 
 while 1:
    vib()
except:
    ser.close()
