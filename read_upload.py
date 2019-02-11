
#!/usr/bin/python2.7.x
import serial
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)

ser1 = serial.Serial("/dev/ttyACM0" , 9600 ,timeout=1)
print("open port")

ch4 = 0
co = 0
temp = 0
vib = 0

import RPi.GPIO as GPIO
import time


#gpio seytup for buxxer        
buzz_pin = 18
led_pin = 11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzz_pin,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)

def buzz():
    for i in range (0,4):
        GPIO.output(buzz_pin,GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(buzz_pin,GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(3)
        print 'ok'





def read_ch4_temp_co():
    ser1.flush()
    a = ser1.readline()
    print("byte read")
    while len(a)<15:
      a = ser1.readline()
      
    print("out of loop")
    a=a.decode("UTF-8")
    print("read")
    r=a.split('  ')
    global ch4
    
    ch4 = float(r[0])
    print("uploaded ch4")
	
        #write program for reading it's values
    global temp
    temp = float(r[1])
    #program for reading temp
    global co
    co= float(r[2])
    
       #program for reading co

def put_ch4():
    
    firebase.put('mines','ch4',ch4)
    print("uploadede ch4")
    if ch4>1200:
        buzz()
    
def put_temp():
    #firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
    firebase.put('mines','temp',temp)
    
def put_co():
    #firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
    firebase.put('mines','co',co)
    if co>85:
        buzz()
    
#def put_vib():
 #   firebase.put('mines','vibrations',vib)
try:    
 while 1:
        #p=subprocess.Popen(['python ~/Desktop/akhi*/vib.py'],shell=True)
        #q=subprocess.Popen(['python ~/Desktop/akhi*/get_alarm.py'],shell=True)
        read_ch4_temp_co()
        put_ch4()
        put_temp()
        put_co()
        #put_vib()
except KeyboardInterrupt:
    ser1.close()
    p.kill()
    q.kill()
    
    