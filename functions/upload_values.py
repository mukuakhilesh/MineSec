import serial
import time
import re
from firebase import firebase

def read_ch4_temp():
    ch4 = 566262.78      #write program for reading it's values
    te0mp = 25.36        #program for reading temp
def read_co():
    co=45.34             #program for reading co

def put_ch4():
    firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
    firebase.put('mines','ch4',ch4)
    
def put_temp():
    firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
    firebase.put('mines','temp',temp)
    
def put_co():
    firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
    firebase.put('mines','co',co)
    
    
read_co()
read_ch4_temp()
put_ch4
put_temp
put_co

    