import RPi.GPIO as GPIO
import time


#gpio seytup for buxxer        
buzz_pin = 18
led_pin = 11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzz_pin,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)
try :
    while 1:
        GPIO.output(buzz_pin,GPIO.HIGH)
        #GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(buzz_pin,GPIO.LOW)
        #GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)
        print ('ok')
        
except KeyboardInterrupt :
    GPIO.output(buzz_pin,GPIO.HIGH)
    GPIO.cleanup()
