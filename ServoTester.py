import ServoController
import LaserController
from pynput import mouse
from pynput.mouse import Button, Controller
import time
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

#Create a range method for floats
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def printStatus():
    print("X:", xAxis.dutyCycle, "Y:", yAxis.dutyCycle)
    laser.printStatus()

def mouseTest():
    mouse = Controller()
    
def mouseToDuty(mousePosition, servo, screenMax):
    ratio = (screenMax)/(servo.MAX_DUTY - servo.MIN_DUTY)
    dutyCycle = (mousePosition/ratio) + 1
    return dutyCycle

def on_move(newx, newy):
    print('Pointer moved to {0}'.format((newx, newy)))
    
    #flip x value
    d = (xAxis.MAX_DUTY+xAxis.MIN_DUTY) - mouseToDuty(newx, xAxis, SCREEN_WIDTH)
    
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
 
 
 
 
 
 
 
         
def printHeader(message):
    bufferTiles = 24 - (int)(len(message)/2) 
    print("###################################################")
    print("###################################################")
    print(bufferTiles*"#",message, bufferTiles*"#")
    print("###################################################")
    print("###################################################")

    
def laserTest():
    printHeader("Laser Test")
    for i in range(25):
        laser.toggleLaser()
        time.sleep(.1)
        
def horizontalTest():
    printHeader("Horizontal Test")
    yAxis.setDutyCycle(yAxis.MID_DUTY)
    for d in frange(xAxis.MIN_DUTY, xAxis.MAX_DUTY, xAxis.ONE_DEGREE):
        xAxis.setDutyCycle(d)
        printStatus()

def verticalTest():
    printHeader("Vertical Test")
    xAxis.setDutyCycle(xAxis.MID_DUTY)
    for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
        yAxis.setDutyCycle(d)
        printStatus()
    
def diagonalTest1():
    printHeader("Q1 to Q3 - Start")
    for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
        yAxis.setDutyCycle(d)
        xAxis.setDutyCycle(d)
        printStatus()

def diagonalTest2():
    printHeader("Q3 to Q1 - Start")
    for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
        yAxis.setDutyCycle(yAxis.MAX_DUTY + yAxis.MIN_DUTY - d)
        xAxis.setDutyCycle(xAxis.MAX_DUTY + xAxis.MIN_DUTY - d)
        printStatus()
    
def diagonalTest3():
    printHeader("Q2 to Q4 - Start")
    for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
        yAxis.setDutyCycle(d)
        xAxis.setDutyCycle(xAxis.MAX_DUTY + xAxis.MIN_DUTY - d)
        printStatus()
        
def diagonalTest4():
    printHeader("Q4 to Q2 - Start")
    for d in frange(xAxis.MIN_DUTY, xAxis.MAX_DUTY, xAxis.ONE_DEGREE):
        yAxis.setDutyCycle(yAxis.MAX_DUTY + yAxis.MIN_DUTY - d)
        xAxis.setDutyCycle(d)
        printStatus()

def main():             
    try:
        mouseTest()
        laserTest()
        horizontalTest()
        verticalTest()
        diagonalTest1()
        diagonalTest2()
        diagonalTest3()
        diagonalTest4()
        
    except KeyboardInterrupt:
        print("keyboard")
        
#    except Exception:
#        print(Exception)
#        xAxis.end()
#        yAxis.end()
#        laser.end()
        
if __name__ == "__main__":
    main()