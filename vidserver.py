#!/usr/bin/env python3
import time
import subprocess
import threading
from flask import Flask, send_from_directory, Response
from opsetspeed.shminject import Mem

# TODO: if no build dir, run make

app = Flask(__name__,)

mem = Mem()
vmax = 28
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
