import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Laser:
    def __init__(self, pin):
        self.pin = pin
        self.power = False
        GPIO.setup(pin, GPIO.OUT)
        self.updateLaser()
        
    def toggleLaser(self):
        self.power = not self.power
        self.updateLaser()
    
    def setPower(self, flag):
        self.power = flag
        self.updateLaser()
    
    def updateLaser(self):
        GPIO.output(self.pin, self.power)
        self.printStatus()
        
    def printStatus(self):
        power = "ON" if self.power else "OFF"
        print("Lights", power)
    
    def end(self):
        GPIO.cleanup()
