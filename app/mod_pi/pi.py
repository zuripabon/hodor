import time
import datetime
from config import GPIO_HIGH_TIME, GPIO_JOIN, GPIO_LEAVE

try:
    import RPi.GPIO as GPIO
    GPIO_ACTIVED = True
except:
    GPIO_ACTIVED = False

def setup():
    GPIO.setmode(GPIO.BCM) ## Use board pin numbering
    GPIO.setup(GPIO_JOIN, GPIO.OUT) ## Setup GPIO Pin 17(11) to OUT
    GPIO.setup(GPIO_LEAVE, GPIO.OUT) ## Setup GPIO Pin 22(15) to OUT

def open_doors(pin):
    print pin
    if not GPIO_ACTIVED:
        return
    setup()
    # start current
    GPIO.output(pin, True)
    time.sleep(GPIO_HIGH_TIME)
    # stop current
    GPIO.output(pin, False)
    GPIO.cleanup()

def join():
    try:
        open_doors(GPIO_JOIN)
    except Exception, e:
        print e

def leave():
    try:
        open_doors(GPIO_LEAVE)
    except Exception, e:
        print e
