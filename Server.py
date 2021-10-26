import socket
import pickle
from _thread import *
from Players import Player

bind_id = "10.0.19.54"
bind_port = 5555
current_player = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_id, bind_port))
server.listen(2)

print("Waiting for a connection, Server Started")


players = [Player(525, 200, 20, 20, (255, 0, 0)), Player(525, 550, 20, 20, (0, 0, 255))]


def threaded_client(conn, player_n):
    conn.send(pickle.dumps(players[player_n]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player_n] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player_n == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


while True:
    conn, addr = server.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_player))

    current_player += 1
