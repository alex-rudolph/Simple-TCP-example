# Taylor Malott
# Alexander Rudolph
# Zosimo Geluz

from socket import*
serverName = '10.31.77.79' ## this should be the ip address
serverPort = 6600

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print("Welcome to the random card generator!")

print("To end the game, enter the number 0")

sentence = input('Please enter a hand size from 1-52: ')
clientSocket.send(sentence.encode())

hand = clientSocket.recv(1024)

print('Your hand is:', hand.decode())

print("")
##
remainder = clientSocket.recv(1024)

print('The remaining cards:', remainder.decode())

clientSocket.close()
