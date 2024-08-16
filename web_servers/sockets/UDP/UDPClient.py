from socket import *


def main():
    serverName = 'hostname'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    message = input('Input lowercase sentence:')

    clientSocket.sendto(message.encode(),(serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print("serverAddress: ", serverAddress)
    print(modifiedMessage.decode())
    clientSocket.close()


if __name__ == "__main__":
    main()