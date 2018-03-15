#/bin/env python

import logging
import sys
import getopt
import os
from layer import BotLayer
from config import load
from yowsup.stacks import  YowStackBuilder
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv

def main(argv):

  phone = None
  password = None
  config = None
  debug = False

  try:

    opts, args = getopt.getopt(argv, "u:c:d", ["user=", "config=", "debug="])

  except getopt.GetoptError:

    print 'run.py -u <phone:password> -d <debug>'
    sys.exit(2)

  for opt, arg in opts:

    if opt in ("-u", "--user"):

      user = arg.split(':')
      phone = user[0]
      password = user[1]

    elif opt in ("-c", "--config"):

      config = load(os.path.abspath(arg))

    elif opt in ("-d", "--debug"):

      debug = True

  logging.basicConfig(level=logging.DEBUG if debug else logging.CRITICAL)

  run(phone if phone is not None else config['phone'], password if password is not None else config['password'])


def run(phone, password):

  # credentials = (phone.encode(), password.encode())

  stackBuilder = YowStackBuilder()

  stack = stackBuilder.pushDefaultLayers(True).push(BotLayer()).build()

  # Setting credentials
  stack.setCredentials((phone, password))

  # Whatsapp server address
  stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

  stack.loop()

if __name__ == "__main__":
  main(sys.argv[1:])