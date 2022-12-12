#!/usr/bin/env python3


## TODO:
# use this instead of file read/write to share setspeed with op

from multiprocessing import shared_memory

name="abcd"
shm = shared_memory.SharedMemory(name=name, create=True, size=1)
shmb = shared_memory.SharedMemory(shm.name)
type(shm.buf)
buf = shm.buf
buf[0] = 4
len(buf)
print(buf)
print(buf[0])
print(dir(buf))
a = buf
print(a)
#buf[:4] = bytearray([22, 33, 44, 55])


shm.close()
shmb.close()
shm.unlink()
