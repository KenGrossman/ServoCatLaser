import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Servo:
    MIN_DUTY = 1 #UP/RIGHT
    MAX_DUTY = 10 #DOWN/LEFT
    MID_DUTY = MIN_DUTY + (MAX_DUTY-MIN_DUTY) / 2
    ONE_DEGREE = (MAX_DUTY-MIN_DUTY) / 180
    SLEEP_SPEED = .0
        
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        servoMotor = GPIO.PWM(int(pin), 50)
        servoMotor.start(self.MID_DUTY)
        self.servoMotor = servoMotor
        
    def setDutyCycle(self, d):
        self.servoMotor.ChangeDutyCycle(d)
        self.dutyCycle = d
        time.sleep(self.SLEEP_SPEED)
    
    def center(self):
        self.setDutyCycle(self.MID_DUTY)
    
    def end(self):
        GPIO.cleanup()
