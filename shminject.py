#!/usr/bin/env python3

from common.conversions import Conversions as CV
from multiprocessing import shared_memory
import atexit

class Hook:
  mem = None
  def update(self, rcs, rcsc):
    vmaxmps = self.mem.vinit * CV.MPH_TO_MS
    # ret cruisestate speed and speed cluster
    a = rcs
    b = rcsc

    if b <= vmaxmps:
      vmph = self.mem.get()
      if vmph <= b:
        vmps = vmph * CV.MPH_TO_MS
        a = vmps
        b = vmps
    return a, b
  def __init__(self):
    self.mem = Mem(autounlink=True)

class Mem:
  __mem = None
  name = "fff"
  size = 1
  vinit = 28 # vmax
  def set(self, v):
    #buf[:4] = bytearray([22, 33, 44, 55])
    self.__mem.buf[0] = v
  def get(self):
    return self.__mem.buf[0]
  def __create_or_connect(self):
    self.__mem = shared_memory.SharedMemory(name=self.name, create=True, size=self.size)
  def __cleanup(self):
    self.__mem.close()
    if self.__shouldunlink:
      self.__mem.unlink()
  def __init__(self, autounlink=False):
    self.__shouldunlink = autounlink
    self.__create_or_connect()
    self.set(self.vinit) # todo maybe dont always do this
    atexit.register(self.__cleanup)

def main():
  mem = Mem(autounlink=True)
  mem.set(0)

main()
