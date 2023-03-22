import RPi.GPIO as GPIO
import time
import alarm_trigger as at
trigPin = 11 #GPIO 17
echoPin = 13 #GPIO 27
MAX_DISTANCE = 220 #define the maximum measured distance(cm)
timeOut = MAX_DISTANCE*60 #calculate timeout(μs) according to the maximum measured distance
def pulseIn(pin,level,timeOut): # function pulseIn: obtain pulse time of a pin
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    pulseTime = (time.time() - t0)*1000000
    return pulseTime

def getSonar(): #get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH) #make trigPin send 10us high level 
    time.sleep(0.00001) #10us
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut) #read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0 # the sound speed is 340m/s, and calculate distance (cm)
    return distance

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD) #numbers GPIOs by physical location
    GPIO.setup(trigPin, GPIO.OUT) # set trigPin to output mode
    GPIO.setup(echoPin, GPIO.IN) # set echoPin to input mode

def loop():
    while(True):
        distance = getSonar()
        print ("The distance is : %.2f cm"%(distance))
        if distance > 10:
            print("Intrusion detected!")
            at.start()
        time.sleep(1)

if __name__ == '__main__': #program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        GPIO.cleanup()