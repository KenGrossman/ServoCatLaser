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
    dm.xAxis.center()
    for d in frange(dm.yAxis.MIN_DUTY, dm.yAxis.MAX_DUTY, dm.yAxis.ONE_DEGREE):
        dm.yAxis.setDutyCycle(d)
        dm.printStatus()
    
#startQuadrant should be 1-4
def diagonalTest(startQuadrant):
    printHeader("Diagonal Test Q%0 - Q%1").format(startQ, endQ)
    
    xReverse = false
    yReverse = false

    if(startQuadrant == 1):
        xReverse = false
        yReverse = false        
    elif(startQuadrant == 2):
        xReverse = true
        yReverse = false        
    elif(startQuadrant == 3):
        xReverse = true
        yReverse = true        
    elif(startQuadrant == 4):
        xReverse = false
        yReverse = true        

    for d in frange(dm.xAxis.MIN_DUTY, dm.xAxis.MAX_DUTY, dm.xAxis.ONE_DEGREE):
        dm.xAxis.setDutyCycle(d if !modified else (dm.xAxis.getRange() - d))
        dm.yAxis.setDutyCycle(d if !modified else (dm.yAxis.getRange() - d))
        printStatus()

# def diagonalTest1():
#     printHeader("Q1 to Q3 - Start")
#     for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
#         dm.yAxis.setDutyCycle(d if !modified else (dm.yAxis.getRange() - d))
#         xAxis.setDutyCycle(d)
#         printStatus()

# def diagonalTest2():
#     printHeader("Q3 to Q1 - Start")
#     for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
#         yAxis.setDutyCycle(yAxis.MAX_DUTY + yAxis.MIN_DUTY - d)
#         xAxis.setDutyCycle(xAxis.MAX_DUTY + xAxis.MIN_DUTY - d)
#         printStatus()
    
# def diagonalTest3():
#     printHeader("Q2 to Q4 - Start")
#     for d in frange(yAxis.MIN_DUTY, yAxis.MAX_DUTY, yAxis.ONE_DEGREE):
#         yAxis.setDutyCycle(d)
#         xAxis.setDutyCycle(xAxis.MAX_DUTY + xAxis.MIN_DUTY - d)
#         printStatus()
        
# def diagonalTest4():
#     printHeader("Q4 to Q2 - Start")
#     for d in frange(xAxis.MIN_DUTY, xAxis.MAX_DUTY, xAxis.ONE_DEGREE):
#         yAxis.setDutyCycle(yAxis.MAX_DUTY + yAxis.MIN_DUTY - d)
#         xAxis.setDutyCycle(d)
#     printStatus()

def main():
    try:
        print("hello")
        laserTest()
        horizontalTest()
        verticalTest()
        diagonalTest(1)
        diagonalTest(2)
        diagonalTest(3)
        diagonalTest(4)
        # diagonalTest1()
        # diagonalTest2()
        # diagonalTest3()
        # diagonalTest4()
        
    except KeyboardInterrupt:
        print("keyboard")
        
    except Exception:
        print(Exception)
        
if __name__ == "__main__":
    main()
