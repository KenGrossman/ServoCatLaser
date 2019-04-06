import ServoController
import LaserController
import tkinter

#Get Screen Info
#root = tkinter.Tk()
#SCREEN_WIDTH = root.winfo_screenwidth()
#SCREEN_HEIGHT = root.winfo_screenheight()

#Assign variables for GPIO pin of peripheral 
xAxisPin = 7
yAxisPin = 5
laserPin = 12

#Create objects for hardware interface
xAxis = ServoController.Servo(xAxisPin)
yAxis = ServoController.Servo(yAxisPin)
laser = LaserController.Laser(laserPin)
##mouse = MouseController.Mouse()

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
