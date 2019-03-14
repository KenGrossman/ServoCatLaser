#from pynput import mouse
#from pynput.mouse import Button, Controller
#import tkinter
import RPi.GPIO as GPIO
import time

##Get Screen Info
#root = tkinter.Tk()
#SCREEN_WIDTH = root.winfo_screenwidth()
#SCREEN_HEIGHT = root.winfo_screenheight()

#Configure GPIO PINS (5 - yAxis, 7 = xAxis, 12 - laser)
GPIO.setmode(GPIO.BOARD)
#
#GPIO.setup(5, GPIO.OUT)
#GPIO.setup(7, GPIO.OUT)
##GPIO.setup(12, GPIO.OUT)
#
##Setup pin 5 and 7 for Pulse width modulation of 50hz
#xAxis = GPIO.PWM(7,50)
#yAxis = GPIO.PWM(5,50)

class Servo:
    
    MIN_DUTY = 1 #UP/RIGHT
    MAX_DUTY = 10 #DOWN/LEFT
    MID_DUTY = MIN_DUTY + (MAX_DUTY-MIN_DUTY) / 2
    ONE_DEGREE = (MAX_DUTY-MIN_DUTY) / 180
    SLEEP_SPEED = .025
        
    def __init__(self, pin):
        #Activate servo connected to pin
#        self.printHeader("Activating servo")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        servoMotor = GPIO.PWM(int(pin), 50)
        
#        self.printHeader("Centering Servo")
        servoMotor.start(self.MID_DUTY)
        self.servoMotor = servoMotor
    def setDutyCycle(self, d):
        self.servoMotor.ChangeDutyCycle(d)
#        printDutyCycle(x, y)
        print("Duty cycle: ", d)
        time.sleep(self.SLEEP_SPEED)

#        mouseX = SCREEN_WIDTH/2
#        mouseY = SCREEN_HEIGHT/2
#        mouse = Controller()
#        mouse.position = (mouseX, mouseY)
#        
#        xAxis.start(self.MID_DUTY)
#        yAxis.start(self.MID_DUTY)
#        
#        self.printHeader("Turning on Laser")
#        GPIO.output(12, 1)
#    
#    def getMinDuty(self):
#        return self.MIN_DUTY
#
#    def getMaxDuty(self):
#        return self.MAX_DUTY

    #Set X and Y duty cycle


    

#    #Set X and Y duty cycle
#    def setDutyCycle1(self, x, y):
#        xAxis.ChangeDutyCycle(x)
#        yAxis.ChangeDutyCycle(y)
#        printDutyCycle(x, y)
#        time.sleep(SLEEP_SPEED)
#        
#    #Print X and Y duty cycle values
#    def printDutyCycle(self, x, y):
#        print("X", x, "Y", y)
#
#    def printHeader(self, message):
#        print("###################################################")
#        print("###################################################")
#        print(message)
#        print("###################################################")
#        print("###################################################")
#
#    def printScreenSize(self):
#        print("Height", SCREEN_HEIGHT, "Width", SCREEN_WIDTH)

#    def on_move(self, x, y):
#        #print('Pointer moved to {0}'.format((x, y)))
#        print(mouseX)
#
#    def on_click(self, x, y, button, pressed):
#        print('{0} at {1}'.format(
#            'Pressed' if pressed else 'Released',
#            (x, y)))
#        if not pressed:
#            # Stop listener
#            return False
        
#MAIN
#mouseX = 0
#mouseY = 0   

#with mouse.Listener(
#    on_move=Servo.on_move,
#    on_click=Servo.on_click) as listener:
#    listener.join()       