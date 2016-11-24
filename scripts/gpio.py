import sys
import time
import datetime
import RPi.GPIO as GPIO

def setup_gpio():
  GPIO.setmode(GPIO.BCM) ## Use board pin numbering
  GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 17(11) to OUT
  GPIO.setup(22, GPIO.OUT) ## Setup GPIO Pin 22(15) to OUT
  
def log(string, *f):
  print(string.format(*f))
  
def test(pin):

  log("Testing pin '{}' on {} ", pin, datetime.datetime.now())
  
  # start current
  GPIO.output(pin, True)

  time.sleep(1)
  
  # stop current
  GPIO.output(pin, False)

if __name__ == "__main__":
  setup_gpio()
  test(17)
  test(22)
  sys.exit()
