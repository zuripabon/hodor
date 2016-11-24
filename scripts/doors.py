import signal
import sys
import time
import datetime
#import urlparse
import paho.mqtt.client as mqtt

try:
  import RPi.GPIO as GPIO
  GPIO_ACTIVED = True
except:
  GPIO_ACTIVED = False

MQTT_HOST = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_TOPIC = "com/itrsgroup/mlg2016"
MQTT_LOG = True
GPIO_JOIN = 17
GPIO_LEAVE = 22

def setup_gpio():
  GPIO.setmode(GPIO.BCM) ## Use board pin numbering
  GPIO.setup(GPIO_JOIN, GPIO.OUT) ## Setup GPIO Pin 17(11) to OUT
  GPIO.setup(GPIO_LEAVE, GPIO.OUT) ## Setup GPIO Pin 22(15) to OUT

def signal_handler(signal, frame):
  log("quitting ...")
  GPIO.cleanup()
  sys.exit(0)

#def reset(publish):
#  publish(MQTT_TOPIC, "garage?0")

def log(string, *f):
  if MQTT_LOG:
    print(string.format(*f))

def open_doors(mqttc, pin):

  if not GPIO_ACTIVED:
    return

  log("Open door '{}' on {} ", "join" if pin == GPIO_JOIN else "leave", datetime.datetime.now())

  # start current
  GPIO.output(pin, True)

  time.sleep(1)

  # stop current
  GPIO.output(pin, False)

def on_connect(mqttc, obj, flags, rc):
  #reset(mqttc.publish)
  log("connected")

def on_message(mqttc, obj, msg):
  try:
    (command, value) = str(msg.payload).split("?")
    #options = urlparse.parse_qs(value)

    log("Got message {} with value {}", command, value)

    if not mqttc.sem and command == "garage":
      mqttc.sem = True
      open_doors(mqttc, GPIO_JOIN if value == "join" else GPIO_LEAVE)
      # reset(mqttc.publish)
      # publish ack to the emitter to let it know the command was executed
      mqttc.sem = False
  except Exception, e:
    print(e)

def on_publish(mqttc, obj, mid):
  log("onpublish: mid {}", str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
  log("onsubscribed: mid {}, graned_qos {}", str(mid), str(granted_qos))

def on_log(mqttc, obj, level, string):
  log(string)

def on_disconnect(mqttc, userdata, rc):
  log("disconnected {}", str(rc))
  connect()

def setup_mqtt_client():

  mqttc = mqtt.Client()
  mqttc.sem = False
  mqttc.on_message = on_message
  mqttc.on_connect = on_connect
  mqttc.on_publish = on_publish
  mqttc.on_subscribe = on_subscribe
  mqttc.on_disconnect = on_disconnect

  if MQTT_LOG:
    mqttc.on_log = on_log

  return mqttc

def connect():
  try:

    mqttc = setup_mqtt_client()
    mqttc.connect(MQTT_HOST, MQTT_PORT)
    mqttc.subscribe(MQTT_TOPIC)
    mqttc.loop_forever()

  except Exception,  e:
    print str(e)
    log("quitting ... ")
    if GPIO_ACTIVED:
      GPIO.cleanup()

if __name__ == "__main__":

  if GPIO_ACTIVED:
    setup_gpio()

  connect()
