import colorsys 
import numpy as np
import RPi.GPIO as GPIO 
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

while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    for h in range(360):
        h_value =h/360
        # print(h_value)
        array =np.multiply([colorsys.hsv_to_rgb(h_value, 1, 1)], [100.0, 100.0,100.0])
        # print((array))
        r, g, b = array.ravel()
        # red = float(r*100)
        # blue =float(b*100)
        # green = float(g*100)

        # print(r, ' ', g, ' ', b)
        # if h==360:
        #     break
        changeColor(r, g, b)
        time.sleep(0.06)
    # break