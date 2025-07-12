# used as reference: https://realpython.com/python-sockets/
import socket
import time

HOST = "localhost"
PORT  = 53333
MESSAGES = 1000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            received = 0
            #while True:
            while received < MESSAGES:
                data = conn.recv(1024)
                if not data:
                    break
                received += data.count(b'hello TCP')
                
            conn.sendall(b'back at you TCP')

if __name__ == "__main__":
    main()
