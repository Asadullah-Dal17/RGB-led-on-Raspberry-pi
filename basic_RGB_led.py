import RPi.GPIO as GPIO 
import random 
import time 

rPin =26
gPin =19
bPin =13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.output(rPin, GPIO.LOW)
GPIO.output(gPin, GPIO.LOW)
GPIO.output(bPin, GPIO.LOW)

red= GPIO.PWM(rPin, 100)
green= GPIO.PWM(gPin, 100)
blue= GPIO.PWM(bPin, 100)

red.start(0)
green.start(0)
blue.start(0)

def changeColor(r_value, g_value, b_value):
    red.ChangeDutyCycle(r_value)
    green.ChangeDutyCycle(g_value)
    blue.ChangeDutyCycle(b_value)
r, g , b =0,0,0
while True:
    values = input("Enter comma separated values(RGB) :  ")
    l = values.split(',')
    print(values)
    if len(l)==3:
        r, g , b = l
        r, g, b =int(r), int(g) , int(b) 
        changeColor(r, g, b)
    elif l[0]=='exit':
        break
    else:
        changeColor(r, g, b)
    print(f'red : {r}    green : {g}     blue :  {b}')
    time.sleep(0.5)