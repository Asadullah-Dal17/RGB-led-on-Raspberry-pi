import colors 
import numpy as np
import cv2 as cv
import RPi.GPIO as GPIO 
import time 

def nothing(x):
    pass
cv.namedWindow('img')
cv.createTrackbar('h', 'img', 10, 255,nothing)
cv.createTrackbar('s', 'img', 20, 100, nothing)
cv.createTrackbar('v', 'img', 3, 100, nothing)


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

while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    h = cv.getTrackbarPos('h', 'img')
    s = (cv.getTrackbarPos('s', 'img')/100)
    v = (cv.getTrackbarPos('v', 'img')/100)
    c_arry =colors.hsv_to_rgb(np.array([[s,v,h]]))
    print(s)
    # print(c_arry)
    r, g, b = c_arry.ravel()
    print(r, b, g)
    # type
    r_c = (int(b), int(g),int(r))

    cv.rectangle(img, (30,30),(300, 300), r_c, -1)
    l_r = r/255
    l_g = g/255
    l_b = b/255
    changeColor(l_r, l_g, l_b)
    cv.imshow('img', img)
    key  = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()