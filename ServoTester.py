import DeviceManager as dm
import time

#Create a range method for floats
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step 
         
def printHeader(message):
    bufferTiles = 24 - (int)(len(message)/2) 
    print("###################################################")
    print("###################################################")
    print(bufferTiles*"#",message, bufferTiles*"#")
    print("###################################################")
    print("###################################################")

#def mouseTest():
#    printHeader("Mouse Test")
#    dm.mouse.Listener
    
def laserTest():
    printHeader("Laser Test")
    for i in range(25):
        dm.laser.toggleLaser()
        time.sleep(.1)
        
def horizontalTest():
    printHeader("Horizontal Test")
    dm.yAxis.center()
    for d in frange(dm.xAxis.MIN_DUTY, dm.xAxis.MAX_DUTY, dm.xAxis.ONE_DEGREE):
        dm.xAxis.setDutyCycle(d)
        dm.printStatus()

def verticalTest():
    printHeader("Vertical Test")
    xAxis.setDutyCycle(xAxis.MID_DUTY)
    for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
        yAxis.setDutyCycle(d)
        dm.printStatus()
    
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

def main():             #        laserTest()
#        horizontalTest()
#        verticalTest()
#        diagonalTest1()
#        diagonalTest2()
#        diagonalTest3()
#        diagonalTest4()
    try:
        print("hello")
#        mouseTest()
#        laserTest()
        horizontalTest()
        verticalTest()
        diagonalTest1()
        diagonalTest2()
        diagonalTest3()
        diagonalTest4()
        
    except KeyboardInterrupt:
        print("keyboard")
        
    except Exception:
        print(Exception)
#        xAxis.end()
#        yAxis.end()
#        laser.end()
        
if __name__ == "__main__":
    main()
