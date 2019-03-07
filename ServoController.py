from pynput import mouse
from pynput.mouse import Button, Controller
import tkinter
import RPi.GPIO as GPIO
import time

#Get Screen Info
root = tkinter.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

#Set Constants
MIN_DUTY = 1 #UP/RIGHT
MAX_DUTY = 10 #DOWN/LEFT
CENTER = MIN_DUTY + (MAX_DUTY-MIN_DUTY) / 2
ONE_DEGREE = MAX_DUTY / 180
SLEEP_SPEED = .025

#Configure GPIO PINS (5 - yAxis, 7 = xAxis, 12 - laser)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
#GPIO.setup(12, GPIO.OUT) -UNCOMMENT WHEN YOU FIX LASER

#Setup pin 5 and 7 for Pulse width modulation of 50hz
xAxis = GPIO.PWM(7,50)
yAxis = GPIO.PWM(5,50)

#Center laser and mouse
def setup():
    printHeader("Centering mouse and laser")
    mouseX = SCREEN_WIDTH/2
    mouseY = SCREEN_HEIGHT/2
    mouse = Controller()
    mouse.position = (mouseX, mouseY) 
    xAxis.start(CENTER)
    yAxis.start(CENTER)
    #GPIO.output(12, 1) -UNCOMMENT WHEN YOU FIX LASER

#Set X and Y duty cycle
def setDutyCycle(x, y):
    xAxis.ChangeDutyCycle(x)
    yAxis.ChangeDutyCycle(y)
    printPosition(x, y)
    time.sleep(SLEEP_SPEED)
    
#Print X and Y duty cycle values
def printPosition(x, y):
    print("X", x, "Y", y)

def printHeader(message):
    print("###################################################")
    print("###################################################")
    print(message)
    print("###################################################")
    print("###################################################")

def printScreenSize():
    print("Height", SCREEN_HEIGHT, "Width", SCREEN_WIDTH)

#Test Y-Axis
def verticalTest():
    printHeader("Vertical - Start")
    y = MIN_DUTY
    x = CENTER
    xAxis.ChangeDutyCycle(x)
    while y <= MAX_DUTY:
        setDutyCycle(x, y)
        y = y + ONE_DEGREE

#Test X-Axis
def horizontalTest():
    printHeader("Horizontal - Start")
    x = MIN_DUTY
    y = CENTER
    yAxis.ChangeDutyCycle(y)
    while x <= MAX_DUTY:
        setDutyCycle(x, y)
        x = x + ONE_DEGREE
        
def diagonalTest1():
    printHeader("Top Right to Bottom Left - Start")
    cycle = MIN_DUTY
    while cycle <= MAX_DUTY:
        setDutyCycle(cycle, cycle)
        cycle = cycle + ONE_DEGREE

def diagonalTest2():
    printHeader("Bottom Left to Top Right - Start")
    cycle = MAX_DUTY
    while cycle >= MIN_DUTY:
        setDutyCycle(cycle, cycle)
        cycle = cycle - ONE_DEGREE
        
def diagonalTest3():
    printHeader("Top Left to Bottom Right - Start")
    x = MAX_DUTY
    y = MIN_DUTY
    while x >= MIN_DUTY:
        setDutyCycle(x, y)
        x = x - ONE_DEGREE
        y = y + ONE_DEGREE
        
def diagonalTest4():
    printHeader("Bottom Right to Top Left - Start")
    x = MIN_DUTY
    y = MAX_DUTY
    while y >= MIN_DUTY:
        setDutyCycle(x, y)
        x = x + ONE_DEGREE
        y = y - ONE_DEGREE

def on_move(x, y):
    #print('Pointer moved to {0}'.format((x, y)))
    print(mouseX)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False
#MAIN
mouseX = 0
mouseY = 0
setup()

with mouse.Listener(
    on_move=on_move,
    on_click=on_click) as listener:
    listener.join()     
        
try:
    verticalTest()
    horizontalTest()
    diagonalTest1()
    diagonalTest2()
    diagonalTest3()
    diagonalTest4()
    GPIO.cleanup()
    
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()