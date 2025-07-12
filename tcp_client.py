# used as reference: https://realpython.com/python-sockets/
import socket
import time

HOST = "localhost"
PORT  = 53333
MESSAGES = 1000

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        begin_time = time.time()

        for i in range(MESSAGES):
            s.sendall(b"hello TCP")

        data = s.recv(1024)
        finish_time = time.time()

        rtt = (finish_time - begin_time) * 1000
        print(rtt)

    print(f"{data.decode()}")

if __name__ == "__main__":
    main()
