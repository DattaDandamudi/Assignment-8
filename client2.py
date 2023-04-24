#client2.py
import socket
import random

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

cards = [(1, "Diamonds"), (2, "Diamonds"), (3, "Diamonds"), (4, "Diamonds"), (5, "Diamonds"), (6, "Diamonds"), (7, "Diamonds"), (8, "Diamonds"), (9, "Diamonds"), (10, "Diamonds"), (11, "Diamonds"), (12, "Diamonds"), (13, "Diamonds")]

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