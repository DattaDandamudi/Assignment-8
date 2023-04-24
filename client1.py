#client1.py
import socket
import random

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

cards = [(1, "Hearts"), (2, "Hearts"), (3, "Hearts"), (4, "Hearts"), (5, "Hearts"), (6, "Hearts"), (7, "Hearts"), (8, "Hearts"), (9, "Hearts"), (10, "Hearts"), (11, "Hearts"), (12, "Hearts"), (13, "Hearts")]

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