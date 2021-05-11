import socket, sys
from IPy import IP

def main(ip, port):
  conct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conct.bind((ip, int(port)))

  print("--- STARTUP SERVER ---\nIp : ", ip, "\nPort : ", str(port), "\nstatus : Wait a connection")
  while True:
    conct.listen(5)
    client, address = conct.accept()
    print("- New connection")

    response = client.recv(255)
    if response != "":
      content = ""
      while content != "close":
        content = input("Server : ")
        client.send(content.encode())
        response = client.recv(255).decode()
        print("Client : ", response)
        sys.exit(0)
    elif response == "close" or response == "end":
      client.close
      conct.close
      print("Close")
          

  client.close()

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