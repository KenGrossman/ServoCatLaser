import ServoController

#Assign variables for GPIO pin of peripheral 
xAxisPin = 7
yAxisPin = 5
laserPin = 12

x = ServoController.Servo(xAxisPin)
y = ServoController.Servo(yAxisPin)

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

def horizontalTest():
    printHeader("Horizontal Test")
    y.setDutyCycle(y.MID_DUTY)
    for d in frange(x.MIN_DUTY, x.MAX_DUTY, x.ONE_DEGREE):
        x.setDutyCycle(d)

def verticalTest():
    printHeader("Vertical Test")
    x.setDutyCycle(x.MID_DUTY)
    for d in frange(y.MIN_DUTY, y.MAX_DUTY, y.ONE_DEGREE):
        y.setDutyCycle(d)
    
def diagonalTest1():
    printHeader("Q1 to Q3 - Start")
    for d in frange(y.MIN_DUTY, y.MAX_DUTY, y.ONE_DEGREE):
        y.setDutyCycle(d)
        x.setDutyCycle(d)

def diagonalTest2():
    printHeader("Q3 to Q1 - Start")
    for d in frange(y.MIN_DUTY, y.MAX_DUTY, y.ONE_DEGREE):
        y.setDutyCycle(y.MAX_DUTY + y.MIN_DUTY - d)
        x.setDutyCycle(x.MAX_DUTY + x.MIN_DUTY - d)    
    
def diagonalTest3():
    printHeader("Q2 to Q4 - Start")
    for d in frange(y.MIN_DUTY, y.MAX_DUTY, y.ONE_DEGREE):
        y.setDutyCycle(d)
        x.setDutyCycle(x.MAX_DUTY + x.MIN_DUTY - d)   
        
def diagonalTest4():
    printHeader("Q4 to Q2 - Start")
    for d in frange(x.MIN_DUTY, x.MAX_DUTY, x.ONE_DEGREE):
        y.setDutyCycle(y.MAX_DUTY + y.MIN_DUTY - d)
        x.setDutyCycle(d)

def main():             
    try:
#        horizontalTest()
#        verticalTest()
#        diagonalTest1()
        diagonalTest2()
        diagonalTest3()
        diagonalTest4()
        
    except KeyboardInterrupt:
        print("keyboard")
        
    except Exception:
        print(Exception)
        
if __name__ == "__main__":
    main()