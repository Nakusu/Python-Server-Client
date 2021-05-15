#!/usr/bin/python

from os import kill
import socket, sys
from threading import Thread
from IPy import IP

command = ""
end = True
clients = []

class ClientCo:
  def __init__(self):
    self.thread = None
    self.active = True
    self.ips = []
  def setThread(self, thread: Thread):
    self.thread = thread

def clientThread(client: socket, address, obj: ClientCo):
  global end
  global command
  print("- New connection from ", address[0])
  oldcmd = ""
  while end != False:
    if oldcmd != command:
      client.send(command.encode())
      response = client.recv(999999)
      print("- client [", address[0], "] : ", response.decode())
      oldcmd = command
  print("Close of ", address[0], " connection !")
  try:
    client.send("close".encode())
    client.close()
    sys.exit(0)
  except:
    sys.exit(0)
  
def serverMonitoring(conct: socket):
  global end
  global command
  global clients
  kills = 0
  while end != False:
    try:
      client, address = conct.accept()
      obj = ClientCo()
      tmp = Thread(target=clientThread, args=[client, address, obj])
      tmp.start()
      obj.setThread(tmp)
      clients.append(obj)
    except:
      continue
  sys.exit(0)
  

def main(ip, port):
  global end
  global command
  conct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conct.bind((ip, int(port)))
  conct.listen(5)

  print("--- STARTUP SERVER ---\nIp : ", ip, "\nPort : ", str(port), "\nstatus : Wait a connection")
  monitoring = Thread(target=serverMonitoring, args=[conct])
  monitoring.start()
  while end != False:
    tmp = input("")
    if tmp == "end":
      end = False
      conct.close()
    elif tmp == "help":
      print("- end : close the server and all connections\n- infos : give stats about the server")
    elif tmp == "infos":
      print("- Adress of the server : ", ip, "\n- Port of the server : ", port, "\n- Number of connections : ", len(clients))
    else:
      command = tmp
    
  print("Close of the server !")

def validIp(ip: str):
  ips = ip.split('.')
  if ip.replace(".", "").isnumeric() == False:
    return False
  for tmp in ips:
    if int(tmp) > 255 or int(tmp) < 0:
      return False
  return True

if __name__ == "__main__":
  ip = input("Listen ip (0.0.0.0): ")
  port = input("Listen port : ")
  while port.isnumeric() == False or validIp(ip) == False:
    ip = input("Listen ip (0.0.0.0): ")
    port = input("Listen port : ")
  main(ip, port)