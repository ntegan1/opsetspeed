#!/usr/bin/env python3
import time
import json
import subprocess
import threading
from flask import Flask, send_from_directory, Response

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

app = Flask(__name__,)

@app.route("/fcamera/<segment>")
def g(segment):
  print(segment)
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
  print(segment)
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
  print(segment)
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
  print(segment)
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


@app.route("/routelist")
def d():
  routes = list_to_json("routes", get_routes())
  response = Response(routes, status=200, mimetype='application/json',)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/routelistv2")
def f():
  routes = list_to_json("routes", get_routes_v2())
  response = Response(routes, status=200, mimetype='application/json',)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/segmentlist")
def e():
  routes = list_to_json("segments", get_segments())
  response = Response(routes, status=200, mimetype='application/json',)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/a.mp4")
def b():
  proc = subprocess.Popen(
    ["ffmpeg",
      "-f", "hevc",
      "-r", "20",
      "-i", "fcamera.hevc",
      "-c", "copy",
      "-map", "0",
      "-vtag", "hvc1",
      "-f", "mp4",
      "-movflags", "empty_moov",
      "-",
    ], stdout=subprocess.PIPE
    #], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  dat = proc.stdout.read()
  response = Response(dat, status=200,)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response
aindex="""<html>
  <body>
    hi
<video id="myvideo" width="320" height="240" controls style="background:black">
  <source class="active" src="a.mp4" type="video/mp4" />
  <source src="http://www.w3schools.com/html/movie.mp4" type="video/mp4" />
</video>
  </body>
    <script>
var myvid = document.getElementById('myvideo');

myvid.addEventListener('ended', function(e) {
  // get the active source and the next video source.
  // I set it so if there's no next, it loops to the first one
  var activesource = document.querySelector("#myvideo source.active");
  var nextsource = document.querySelector("#myvideo source.active + source") || document.querySelector("#myvideo source:first-child");
  
  // deactivate current source, and activate next one
  activesource.className = "";
  nextsource.className = "active";
  
  // update the video source and play
  myvid.src = nextsource.src;
  myvid.play();
});
    </script>
</html>
"""

@app.route("/")
def c():
  return aindex

@app.route("/a")
def a():
  proc = subprocess.Popen(
    ["echo", "hihihi"], stdout=subprocess.PIPE, stderr=open("/dev/null")
  )
  dat = proc.stdout.read()
  response = Response(dat, status=200,)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

def main():
  app.run(host="0.0.0.0")

if __name__ == '__main__':
  main()
