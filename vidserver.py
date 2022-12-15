#!/usr/bin/env python3
import time
import json
import subprocess
import threading
from flask import Flask, send_from_directory, Response

build_dir="/data/openpilot/opsetspeed/build"
app = Flask(__name__)


@app.route("/")
def aaa():
  print("slash")
  return send_from_directory(build_dir, "index.html")

def get_routes():
  proc = subprocess.Popen(
    ["/data/openpilot/optool/bin/lsroute",
      "/data/media/0/realdata",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  dat = proc.stdout.read().decode("utf-8").rstrip()
  return dat.split("\n")
def get_segments():
  proc = subprocess.Popen(
    ["/data/openpilot/optool/bin/lssegs",
      "/data/media/0/realdata",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  dat = proc.stdout.read().decode("utf-8").rstrip()
  return dat.split("\n")
def get_routes_v2():
  listt = []
  routes = get_routes()
  segments = get_segments()
  for route in routes:
    obj = { "name": route, "segments": [seg for seg in segments if not seg.find(route) == -1]}
    listt.append(obj)
  return listt

def list_to_json(name, listt):
  #js = [
  #  {"name": name, "list": list}
  #]
  js = {"name": name, "list": listt}
  return json.dumps(js)

@app.route("/fcamera/<segment>")
def g(segment):
  proc = subprocess.Popen(
    ["ffmpeg",
      "-f", "hevc",
      "-r", "20",
      "-i", "/data/media/0/realdata/" + segment + "/fcamera.hevc",
      "-c", "copy",
      "-map", "0",
      "-vtag", "hvc1",
      "-f", "mp4",
      "-movflags", "empty_moov",
      "-",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  response = Response(proc.stdout.read(), status=200,)
  #routes = list_to_json("routes", get_routes())
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/dcamera/<segment>")
def h(segment):
  proc = subprocess.Popen(
    ["ffmpeg",
      "-f", "hevc",
      "-r", "20",
      "-i", "/data/media/0/realdata/" + segment + "/dcamera.hevc",
      "-c", "copy",
      "-map", "0",
      "-vtag", "hvc1",
      "-f", "mp4",
      "-movflags", "empty_moov",
      "-",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  response = Response(proc.stdout.read(), status=200,)
  #routes = list_to_json("routes", get_routes())
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


@app.route("/ecamera/<segment>")
def i(segment):
  proc = subprocess.Popen(
    ["ffmpeg",
      "-f", "hevc",
      "-r", "20",
      "-i", "/data/media/0/realdata/" + segment + "/ecamera.hevc",
      "-c", "copy",
      "-map", "0",
      "-vtag", "hvc1",
      "-f", "mp4",
      "-movflags", "empty_moov",
      "-",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  response = Response(proc.stdout.read(), status=200,)
  #routes = list_to_json("routes", get_routes())
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/qcamera/<segment>")
def j(segment):
  proc = subprocess.Popen(
    ["ffmpeg",
      "-r", "20",
      "-i", "/data/media/0/realdata/" + segment + "/qcamera.ts",
      "-c", "copy",
      "-map", "0",
      "-f", "mp4",
      "-movflags", "empty_moov",
      "-",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  response = Response(proc.stdout.read(), status=200,)
  #routes = list_to_json("routes", get_routes())
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


@app.route("/routelistv2")
def f():
  routes = list_to_json("routes", get_routes_v2())
  response = Response(routes, status=200, mimetype='application/json',)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/<path:name>")
def ab(name):
  print("serving " +name)
  return send_from_directory(build_dir, name)

@app.route("/static/js/<path:name>")
def ae(name):
  print("serving " +name)
  return send_from_directory(build_dir + "/static/js", name)

@app.route("/static/css/<path:name>")
def af(name):
  print("serving " +name)
  return send_from_directory(build_dir + "/static/css", name)

def main():
  app.run(host="0.0.0.0")

if __name__ == '__main__':
  main()
