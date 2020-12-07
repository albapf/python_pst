import socket, sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 8080))
exit = False
while not exit:
    user_text = input("What do you want to send: ")
    if user_text == "exit":
        exit = True
    else:
        client_socket.send(user_text.encode())
        answer = client_socket.recv(1024)
        print(answer.decode())
client_socket.close()