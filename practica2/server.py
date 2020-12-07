import socket, sys, getopt, game

def main():
    number_players = 1
    number_stages = 1
    ip = '127.0.0.1'
    port = 8080
    name = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:s:i:r:n:", ["players=", "stages=", "ip=", "port=", "name="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(0)

    for opt, arg in opts:
        if opt in ('-p', '--players'):
            number_players = arg
        elif opt in ('-s', '--stages'):
            number_stages = arg
        elif opt in ('--ip'):
            ip = arg
        elif opt in ('--port'):
            port = arg
        elif opt in ('--name'):
            name = arg
        else:
            sys.exit(0)

    if int(number_players) >= 1 and int(number_players) <= 4:
        print('number players: {}'.format(number_players))
    else:
        print("The number of players must be between 1 and 4. Finishing program.")
        sys.exit(0)

    if int(number_stages) >= 1 and int(number_stages) <= 10:
        print('number stages: {}'.format(number_stages))
    else:
        print("The number of stages must be between 1 and 10. Finishing program.")
        sys.exit(0)

    try:
        iport = int(port)
        print('port: {}'.format(iport))
    except ValueError:
        print("The port must be an integer.")
        sys.exit(0)

    print('ip : {}'.format(ip))

    if (type(name) != str and type(name) != int):
        print("The name must be formed by letters and numbers.")
        sys.exit(0)
    else:
        print('name: {}'.format(name))


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 8080))
    server_socket.listen(20)

    try:
        while True:
            close_connection = False
            print("Waiting connection ....")
            client_socket, client_address = server_socket.accept()
            print("Connection established: ", client_address)
            while not close_connection:
                try:
                    message = client_socket.recv(1024)
                    print("Message received: ", message.decode())
                    reply = int(input("Welcome to the server. Choose one of this options: \n1.- Create game\n2.- Join game\n3.- Exit\n"))
                    client_socket.send(repr(reply).encode())

                except (ConnectionAbortedError, ValueError) as err:
                    close_connection = True
                    print(err)

                if (reply == 1):
                    print(game)



    except KeyboardInterrupt:
        print("Server closed by admin")



main()