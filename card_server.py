# Taylor Malott
# Alexander Rudolph
# Zosimo Geluz

from socket import*
from random import randint

serverPort = 6600
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

## make the list of cards
deck = ["2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
        "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS",
        "2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
        "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD",]

copy_deck = []  ## should be empty, had errors when a value was added

client_deck = ""

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()

    hand_size = int(connectionSocket.recv(1024).decode())
    if hand_size == 0:
        break
    print("Hand size is:", hand_size)
    print("")


    ## while loop that takes a random card from the deck
    x = 0
    while x < hand_size:
        rnum = randint(0,51)  ## grab a random number
        if rnum in copy_deck:
            print("Number already in copy deck: ")
            print(rnum, "is in copy deck")
        else:
            copy_deck.append(rnum)
            card = deck[rnum] + ' '
            print("The card was", card)
            client_deck +=  str(card)
            ## connectionSocket.send(card.encode())  ## sends the card to the client
            x = x + 1
            print("X = ", x)
    connectionSocket.send(client_deck.encode())  ## sends the card to the client
    client_deck = ""

    ##  print out the remaining cards in the deck
    remainder = ""
    i = 0
    while i < len(deck):
        if i in copy_deck:
            print(i, "already given to player")
        else:
            card = deck[i] + ' '
            remainder += str(card)
        i = i + 1
    connectionSocket.send(remainder.encode())
    connectionSocket.close()
