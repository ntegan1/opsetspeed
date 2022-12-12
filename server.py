#!/usr/bin/env python3
import time
import threading
from flask import Flask, send_from_directory

import cereal.messaging as messaging

build_dir="./build"
static_dir=build_dir + "/static"
allowed_build = ["asset-manifest.json", "favicon.ico", "logo192.png", "logo512.png", "robots.txt"]
app = Flask(__name__, static_folder=static_dir)
pm = messaging.PubMaster(['testJoystick'])

@app.route("/")
def a():
  return send_from_directory(build_dir, "index.html")

last_send_time = time.monotonic()
@app.route("/control/<x>/<y>")
def control(x, y):
  global last_send_time
  x,y = float(x), float(y)
  x = max(-1, min(1, x))
  y = max(-1, min(1, y))
  dat = messaging.new_message('testJoystick')
  dat.testJoystick.axes = [y,x]
  dat.testJoystick.buttons = [False]
  pm.send('testJoystick', dat)
  last_send_time = time.monotonic()
  return ""

@app.route("/<path:name>")
def b(name):
  allowed = name in allowed_build
  return send_from_directory(build_dir, name) if allowed else "f"

def handle_timeout():
  while 1:
    this_time = time.monotonic()
    if (last_send_time+0.5) < this_time:
      #print("timeout, no web in %.2f s" % (this_time-last_send_time))
      dat = messaging.new_message('testJoystick')
      dat.testJoystick.axes = [0,0]
      dat.testJoystick.buttons = [False]
      pm.send('testJoystick', dat)
    time.sleep(0.1)

def main():
  threading.Thread(target=handle_timeout, daemon=True).start()
  app.run(host="0.0.0.0")

if __name__ == '__main__':
  main()
