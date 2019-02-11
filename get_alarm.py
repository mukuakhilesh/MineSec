from firebase import firebase
import smtplib
import RPi.GPIO as GPIO
import time


#gpio seytup for buxxer        
buzz_pin = 18
led_pin = 11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzz_pin,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)
    
    
firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)  #firebase account credentials

ch4 = 0
temp = 0
co = 0
ch4_flag = False
temp_flag = False
co_flag = False
any_high = False
vib_flag=False

def buzz():
    if co_flag or ch4_flag or temp_flag or vib_flag:
        GPIO.output(buzz_pin,GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(buzz_pin,GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(3)
        print 'ok'

def get_ch4():
    global ch4
    ch4=firebase.get('mines','ch4')
    
def get_temp():
    global temp
    temp=firebase.get('mines','temp')
    
def get_co():
    global co
    co=firebase.get('mines','co')
def get_vib():
    global vib
    vib=firebase.get('mines','vibrations')
    print vib
def flags():
    if co > 60:   # put max value here
        global co_flag
        co_flag= True
    else:
        co_flag=False
        
    if ch4 > 150000:
        global ch4_flag
        ch4_flag= True
    else:
        ch4_flag = True
     
    if temp > 107 :
        global temp_flag
        temp_flag= True
    else:
         temp_flag=False
    if float(vib)>4:
        global vib_flag
        vib_flag= True
    else:
        vib_flag = False
    
        
def mail():
    
    if co_flag or ch4_flag or temp_flag or vib_flag:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        receiver = ('akhibiada007@gmail.com','amanborn007@gmail.com','pp981057@gmail.com')
        sub="alert"
        
        msg=""
        if co_flag:
         msg+="carbon monoxide "
        if ch4_flag:
         msg+="methane"
        if temp_flag:
         msg+="temp"
        if vib_flag:
         msg+="vibrations exceeded"
        msg+=" exceeded"
        msg=msg+" on alert"
        sender = 'ashish.aryan099@gmail.com'

        txt="""From:from ashish.aryan099@gmail.com
        To:to akhi.biada007@gmail.com
        Subject:%s

        %s
        """%(sub,msg)
        try:
                server.login('ashish.aryan099@gmail.com','8969675310')
                for id in receiver:
                 print id
                 server.sendmail('ashish.aryan099@gmail.com',str(id),txt)
                server.quit()
                print ("message sent")
        except SMTPException:
                print('mail not sent')


def buzz():
    if co_flag or ch4_flag or temp_flag or vib_flag:
        GPIO.output(buzz_pin,GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(buzz_pin,GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(3)
        print 'ok'

try:
    while 1:
        temp_flag=False
        co_flag=False
        ch4_flag=False
        vib_flag=False
        get_ch4()
        get_temp()
        get_co()
        get_vib()
        flags()
        mail()
        buzz()
        print 'running'
        print vib_flag
        
except KeyboardInterrupt:
    exit(1)