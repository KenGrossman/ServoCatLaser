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

#def boundsTest():
#    for d in frange(-5, 15, dm.xAxis.ONE_DEGREE):
#	dm.xAxis.setDutyCycle(d)
    
#startQuadrant should be 1-4
def diagonalTest(startQuadrant):
    printHeader("Diagonal Test Q{0} - Q{1}".format(startQuadrant, startQuadrant + 2 if startQuadrant < 3 else startQuadrant -2))
    
    #Set reversal boolean based on Start Quadrant
    xReverse = False if startQuadrant == 1 or startQuadrant == 4 else True
    yReverse = False if startQuadrant == 1 or startQuadrant == 2 else True

    #TODO: Reword this loop and maybe above variables to be more readable
    for d in frange(dm.xAxis.MIN_DUTY, dm.xAxis.MAX_DUTY, dm.xAxis.ONE_DEGREE):
        dm.xAxis.setDutyCycle(d if xReverse == False else dm.xAxis.MAX_DUTY + dm.xAxis.MIN_DUTY - d)
        dm.yAxis.setDutyCycle(d if yReverse == False else dm.yAxis.MAX_DUTY + dm.yAxis.MIN_DUTY - d)
        dm.printStatus()

def main():
    try:
        while(True):
            laserTest()
            horizontalTest()
            verticalTest()
            for i in range (1, 4):
                diagonalTest(i)
        
    except KeyboardInterrupt:
        print("keyboard")
        
    except Exception:
        print(Exception)
        
if __name__ == "__main__":
    main()
