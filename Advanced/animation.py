import RPi.GPIO as GPIO 
import colors
import time 
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

# for i in range(255):
#     values =colors.hsv_to_rgb(np.array([[0.5, 0.2, i]]))
#     r, g, b = values.ravel()
#     print(r, (r/2.55))
while True:
    # img = np.zeros((200,200, 3), dtype=np.uint8)
    # cv.imshow('img', img)
    # key =cv.waitKey(1)
    for i in range(255):
        # g = (100 - i)
        values =colors.hsv_to_rgb(np.array([[0.99, (i/255) ,100]]))
        r, g, b = values.ravel()
        r = r/2.55
        g =g/2.55
        b =b/2.55
        print('r,', r, '  g', g , '  b' , b)
        # color = (, g, i)
        # print(g)
        changeColor(r, g,b)
        time.sleep(0.1)
    # for i in range(100, 1, -1):
    #     g = (100 - i)
    #     print(g)
    #     color = (0, g, i)
    #     changeColor(i, g,i)
    #     time.sleep(0.1)
