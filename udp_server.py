# used as reference: https://realpython.com/python-sockets/
import socket
import time

HOST = "localhost"
PORT  = 53444
MESSAGES = 1000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        received = 0
        #while True:
        received = 0
        while received < MESSAGES:
            data, addr = s.recvfrom(1024)
            # if data == b'hello UDP':
            #     s.sendto(b'back at you UDP', addr)
            received += data.count(b'hello UDP')
        s.sendto(b'back at you UDP', addr)

if __name__ == "__main__":
    main()
