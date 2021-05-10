import socket, sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('0.0.0.0', 4579))

print("--- STARTUP SERVER ---\n")
while True:
        socket.listen(5)
        client, address = socket.accept()
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
        elif response == "close":
          client.close
        elif response == "end":
          stock.close
        

print("Close")
client.close()
stock.close()