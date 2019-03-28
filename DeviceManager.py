import ServoController
import LaserController
from pynput import mouse
from pynput.mouse import Button, Controller
import tkinter

#Get Screen Info
root = tkinter.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

#Assign variables for GPIO pin of peripheral 
xAxisPin = 7
yAxisPin = 5
laserPin = 12

#Create objects for hardware interface
xAxis = ServoController.Servo(xAxisPin)
yAxis = ServoController.Servo(yAxisPin)
laser = LaserController.Laser(laserPin)
#mouse = MouseController.Mouse()

def printStatus():
    print("X:", xAxis.dutyCycle, "Y:", yAxis.dutyCycle)
    laser.printStatus()

def printBETTERPRINTMETHOD():
#Put code inside of me
    return

def moveLaser(x, y):
    xAxis.setDutyCycle(x)
    yAxis.setDutyCycle(y)
    
def end():
    xAxis.end()
    yAxis.end()
    laser.end()
###############################MOUSE CODE###############################
    
    #THIS ONE NEEDS UPDATED!!!!!!!!!!!!!!!!!!!!!!!
def mouseToDuty(mousePosition, servo, screenMax):
    ratio = (screenMax)/(servo.MAX_DUTY - servo.MIN_DUTY)
    dutyCycle = (mousePosition/ratio) + 1
    return dutyCycle

    #THIS ONE NEEDS UPDATED!!!!!!!!!!!!!!!!!!!!!!!
def on_move(newx, newy):
    print('Pointer moved to {0}'.format((newx, newy)))
    
    #flip x value
    d = (xAxis.MAX_DUTY + xAxis.MIN_DUTY) - mouseToDuty(newx, xAxis, SCREEN_WIDTH)
    
    xAxis.setDutyCycle(d)
    yAxis.setDutyCycle(mouseToDuty(newy, yAxis, SCREEN_HEIGHT))
    printStatus()

def on_click(x, y, button, pressed):
    if button == Button.right:
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False
    elif button == Button.left:
        if pressed:
            laser.toggleLaser()
with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()
