import time
import threading




def my_Serial():
    for i in range(10):
        time.sleep(1)
        print("thread")

t1 = threading.Thread(target=my_Serial)
#t1.daemon = True
t1.start()

for i in range(10):
    time.sleep(1)
    print("non thread")