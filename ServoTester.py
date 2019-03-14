import ServoController

#Assign variables for GPIO pin of peripheral 
xAxisPin = 7
yAxisPin = 5
laserPin = 12

#Create a range method for floats
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def singleClassTest():
    printHeader("Creating X servo object")
    x = ServoController.Servo(xAxisPin)
    print("Creating Y servo object")
    y = ServoController.Servo(yAxisPin)
    
    for d in frange(x.MIN_DUTY, x.MAX_DUTY, x.ONE_DEGREE):
        x.setDutyCycle(d)
        y.setDutyCycle(d)

def horizontalTest():
    Servo.printHeader("Horizontal - Start")
    Servo.printHeader("Before x")
    x = MIN_DUTY
    print(x)
    Servo.printHeader("X: ", x)
    y = CENTER
    print(y)
    Servo.printHeader("X: ", x, "Y: ", y)
    Servo.setDutyCycle(x, y)
    Servo.printHeader("Before while loop")
    while x <= MAX_DUTY:
        Servo.setDutyCycle(x, y)
        x = x + Servo.ONE_DEGREE

def verticalTest():
    printHeader("Vertical - Start")
    y = MIN_DUTY
    x = CENTER
    xAxis.ChangeDutyCycle(x)
    printHeader("Before while loop")
    while y <= MAX_DUTY:
        setDutyCycle(x, y)
        y = y + ONE_DEGREE
    
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

def printHeader(message):
        bufferTiles = 24 - (int)(len(message)/2) 
        print("###################################################")
        print("###################################################")
        print(bufferTiles*"#",message, bufferTiles*"#")
        print("###################################################")
        print("###################################################")
def main():             
    try:
        print("Top of try")
        singleClassTest()
#        horizontalTest()
#        verticalTest()
#        diagonalTest1()
#        diagonalTest2()
#        diagonalTest3()
#        diagonalTest4()
        #GPIO.cleanup()
        
    except KeyboardInterrupt:
        print("keyboard")
        p.stop()
        #GPIO.cleanup()
#    except Exception:
#        print(Exception)
        #GPIO.cleanup()
if __name__ == "__main__":
    main()