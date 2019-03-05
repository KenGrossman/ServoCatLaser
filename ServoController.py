import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

MIN_DUTY = 1
MAX_DUTY = 11
CENTER = MIN_DUTY + (MAX_DUTY-MIN_DUTY) / 2
ONE_DEGREE = MAX_DUTY / 90

#Setup pin 7 for Pulse width modulation of 50hz
xAxis= GPIO.PWM(7,50)
yAxis= GPIO.PWM(5,50)


#Set starting location to 
xAxis.start(CENTER)
yAxis.start(CENTER)
GPIO.output(12, 1)

def test1():
    cycle = MIN_DUTY
    print("Top Right to Bottom Left - Start")
    while cycle <= MAX_DUTY:
        xAxis.ChangeDutyCycle(cycle)
        yAxis.ChangeDutyCycle(cycle)
        print ("X", cycle, "Y", cycle)
        cycle = cycle + ONE_DEGREE
        time.sleep(.1)

def test2():
    cycle = MAX_DUTY
    print("Bottom Left to Top Right - Start")
    while cycle >= MIN_DUTY:
        xAxis.ChangeDutyCycle(cycle)
        yAxis.ChangeDutyCycle(cycle)
        print ("X", cycle, "Y", cycle)
        cycle = cycle - ONE_DEGREE
        time.sleep(.1)
        
def test3():
    x = MAX_DUTY
    y = MIN_DUTY
    print("Top Left to Bottom Right - Start")
    while x >= MIN_DUTY:
        xAxis.ChangeDutyCycle(x)
        yAxis.ChangeDutyCycle(y)
        print ("X", x, "Y", y)
        x = x - ONE_DEGREE
        y = y + ONE_DEGREE
        time.sleep(.1)
        
def test4():
    x = MIN_DUTY
    y = MAX_DUTY
    print("Bottom Right to Top Left - Start")
    while y >= MIN_DUTY:
        xAxis.ChangeDutyCycle(x)
        yAxis.ChangeDutyCycle(y)
        print ("X", x, "Y", y)
        x = x + ONE_DEGREE
        y = y - ONE_DEGREE
        time.sleep(.1)

#Cycle from top right to bottom left
try:
    test1()
    test2()
    test3()
    test4()
    GPIO.cleanup()
    
except KeyboardInterrupt:
    p.stop()

    GPIO.cleanup()

