import RPi.GPIO as GPIO
import time
alarmPin = 29 #GPIO5

def setup():
    print ('Triggering Alarm')
    GPIO.setmode(GPIO.BOARD) #numbers GPIOs by physical location
    GPIO.setup(alarmPin, GPIO.OUT) # set trigPin to output mode

def loop():
    print("ON")
    GPIO.output(alarmPin, GPIO.HIGH)
    time.sleep(1)
    print("OFF")
    GPIO.output(alarmPin, GPIO.LOW)
    time.sleep(1)

def start(): #program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        GPIO.cleanup()

        