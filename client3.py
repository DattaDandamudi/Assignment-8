#client3.py
import socket
import random

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

cards = [(1, "Clubs"), (2, "Clubs"), (3, "Clubs"), (4, "Clubs"), (5, "Clubs"), (6, "Clubs"), (7, "Clubs"), (8, "Clubs"), (9, "Clubs"), (10, "Clubs"), (11, "Clubs"), (12, "Clubs"), (13, "Clubs")]

for i in range(13):
    print("Round", i+1)
    card = random.choice(cards)
    cards.remove(card)
    print("Server's card:", card)
    while True:
        client_card = input("Enter card (value suit): ")
        if client_card in [str(card[0]) + " " + card[1] for card in cards]:
            s.send(client_card.encode())
            break
        else:
            print("Invalid card!")
    data = s.recv(1024).decode()
    print(data)

s.close()