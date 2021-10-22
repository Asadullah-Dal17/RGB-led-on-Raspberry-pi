import RPi.GPIO as GPIO 
import random 
import time 
import cv2 as cv 
import numpy as np
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
    img = np.zeros((200,200, 3), dtype=np.uint8)
    cv.imshow('img', img)
    key =cv.waitKey(1)
    for i in range(100):
        g = (100 - i)
        color = (0, g, i)
        cv.rectangle(img, (5,5), (25, 25), color, -1)
        cv.imshow('img', img)
        print(g)
        changeColor(i, g,i)
        time.sleep(0.5)
    for i in range(100, 1, -1):
        g = (100 - i)
        print(g)
        color = (0, g, i)
        cv.rectangle(img, (5,5), (25, 25), color, -1)
        cv.imshow('img', img)
        changeColor(i, g,i)
        time.sleep(0.51)
    if key ==ord('q'):
        break
        # img =img[]
    cv.imshow('img', img)
cv.destroyAllWindows()
