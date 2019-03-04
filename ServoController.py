import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

MIN_DUTY = 1
MAX_DUTY = 12
CENTER = MIN_DUTY + (MAX_DUTY-MIN_DUTY) / 2
ONE_DEGREE = MAX_DUTY / 180

#Setup pin 7 for Pulse width modulation of 50hz
xAxis= GPIO.PWM(7,50)
yAxis= GPIO.PWM(5,50)


#Set starting location to 
xAxis.start(CENTER)
yAxis.start(CENTER)

try:
    cycle = MIN_DUTY
    while cycle <= MAX_DUTY:
        xAxis.ChangeDutyCycle(cycle)
        yAxis.ChangeDutyCycle(cycle)
        print ("DEGREES", cycle)
        cycle = cycle + ONE_DEGREE
        time.sleep(.1)
        if (cycle >= 12):
            cycle = 0
        
#        p.ChangeDutyCycle(cycle)
#        print ("DEGREES", cycle)
#        cycle = cycle + ONE_DEGREE
#        time.sleep(.1)
                #90 degrees
#        p.ChangeDutyCycle(11)
#        time.sleep(1)
#        print("Right 90 degrees")
        
                #-90 degrees
#        p.ChangeDutyCycle(2)
#        time.sleep(1)
#        print("x1 degrees")
#        
#        
#        #-90 degrees
#        p.ChangeDutyCycle(2.5)
#        time.sleep(1)
#        print("0 degrees")
#        
#                #-90 degrees
#        p.ChangeDutyCycle(3)
#        time.sleep(1)
#        print("x degrees")
#        
#        #-45 degrees
#        p.ChangeDutyCycle(5.75)
#        time.sleep(1)
#        print("Left 45 degrees")
#        
#        #0 degrees
#        p.ChangeDutyCycle(7.5)
#        time.sleep(1)
#        print("Left 90 degrees")
#        
#        #45 degrees
#        p.ChangeDutyCycle(10)
#        time.sleep(1)
#        print("Left X degrees")  

        
except KeyboardInterrupt:
    p.stop()

    GPIO.cleanup()

