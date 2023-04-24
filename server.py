#server.py
import socket
import random

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

clients = []
scores = {"Client 1": 0, "Client 2": 0, "Client 3": 0}

cards = [(1, "Spades"), (2, "Spades"), (3, "Spades"), (4, "Spades"), (5, "Spades"), (6, "Spades"), (7, "Spades"), (8, "Spades"), (9, "Spades"), (10, "Spades"), (11, "Spades"), (12, "Spades"), (13, "Spades")]
random.shuffle(cards)

print("Server is ready...")
print("Server's cards:", cards)

for i in range(3):
    client_socket, address = s.accept()
    clients.append(client_socket)
    print(f"Connection established with {address}")

for i in range(13):
    print("\nRound", i+1)
    server_card = cards.pop(0)
    print("Server's card:", server_card)

    client_cards = []
    for j in range(3):
        while True:
            data = clients[j].recv(1024).decode()
            client_card = tuple(data.split())
            if client_card not in client_cards:
                client_cards.append(client_card)
                clients[j].send(b"Card received!")
                break
            else:
                clients[j].send(b"Card already used!")
        print(f"Client {j+1}'s card:", client_card)

    winner_card = max(client_cards)
    winner_index = client_cards.index(winner_card)

    if client_cards.count(winner_card) == 1:
        winner = f"Client {winner_index+1}"
        scores[winner] += server_card[0]
        print(f"{winner} wins and gets {server_card[0]} points!")
    elif client_cards.count(winner_card) == 2:
        print("There's a tie between two players!")
        for j in range(3):
            if client_cards[j] == winner_card:
                scores[f"Client {j+1}"] += server_card[0]
                print(f"Client {j+1} gets {server_card[0]} points!")
    else:
        print("It's a tie!")
        for j in range(3):
            scores[f"Client {j+1}"] += server_card[0]
            print(f"Client {j+1} gets {server_card[0]} points!")

print("\nFinal scores:")
for player, score in scores.items():
    print(player, score)

winner = max(scores, key=scores.get)
print(f"\n{winner} wins the game with {scores[winner]} points!")

for client in clients:
    client.send(f"The winner is {winner} with {scores[winner]} points!".encode())

for client in clients:
    client.close()

s.close()