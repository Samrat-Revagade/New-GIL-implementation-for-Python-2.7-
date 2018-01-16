import threading
import time

def f():
    while 1:
        pass


for i in range(10):
    print "starting thread=", i
    t = threading.Thread(target=f)
    t.start()

time.sleep(60)
