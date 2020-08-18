import threading
import time
import queue
import zlib
import binascii
import crcmod
import struct
import requests

a = (0x1, 0x2, 0x3)
c = crcmod.mkCrcFun(0x18005)
aa = struct.pack("%dH" % (len(a)), *a)
print(aa, type(aa))
print(bytes(a))
e = b'12345'
print(type(e))
print(e.hex(), bytes.hex(e))
f = binascii.hexlify(e)
#zlib.crc32()
print(f.decode('utf-8'), type(f))
#b = binascii.crc_hqx(a, 0x0)
#b = zlib.crc32(a.encode())
print(hex(c(bytes(a))))
x = 'abcde'
print(x.encode())
#print(bytes.fromhex(x))


def thread_func():
    global hello
    hello = '你好'
    time.sleep(1)
    print('i am thread_func')

t = threading.Thread(target=thread_func)
t.start()

n = 0
#q = queue.Queue()
#q.task_done()
print(hello)
# while True:
#     print(n)
#     #time.sleep(1)
#     n += 1

