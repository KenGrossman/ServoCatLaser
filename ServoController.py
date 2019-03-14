import RPi.GPIO as GPIO
import time

#from pynput import mouse
#from pynput.mouse import Button, Controller
#import tkinter

##Get Screen Info
#root = tkinter.Tk()
#SCREEN_WIDTH = root.winfo_screenwidth()
#SCREEN_HEIGHT = root.winfo_screenheight()

GPIO.setmode(GPIO.BOARD)

class Servo:
    MIN_DUTY = 1 #UP/RIGHT
    MAX_DUTY = 10 #DOWN/LEFT
    MID_DUTY = MIN_DUTY + (MAX_DUTY-MIN_DUTY) / 2
    ONE_DEGREE = (MAX_DUTY-MIN_DUTY) / 180
    SLEEP_SPEED = .025
        
    def __init__(self, pin):
#        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        servoMotor = GPIO.PWM(int(pin), 50)
        servoMotor.start(self.MID_DUTY)
        self.servoMotor = servoMotor
        
    def setDutyCycle(self, d):
        self.servoMotor.ChangeDutyCycle(d)
        print("Duty cycle: ", d)
        time.sleep(self.SLEEP_SPEED)
    
    def end(self):
        GPIO.cleanup()
        
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

#with mouse.Listener(
#    on_move=Servo.on_move,
#    on_click=Servo.on_click) as listener:
#    listener.join()       