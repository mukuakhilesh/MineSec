import RPi.GPIO as GPIO
import time

Co = 40;  # add co value from cloud here
CH4 = 50000;

buzz_pin = 18
led_pin = 11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzz_pin,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)


def buzz():
    GPIO.output(buzz_pin,GPIO.HIGH)
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(30)
    GPIO.output(buzz_pin,GPIO.LOW)
    GPIO.output(buzz_pin, GPIO.LOW)

def email():
    print("email to be setup")


if (Co>30)and(CH4>50000):
    # both Co and ch4 alarm
    buzz()
    email()
elif Co>30:
    #CO alarm
    buzz()
    email()
else :
    # CH$ alarm
    buzz()
    email()
    
#add email setup here
GPIO.cleanup()