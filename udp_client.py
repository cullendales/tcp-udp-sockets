# used as reference: https://realpython.com/python-sockets/
import socket
import time

HOST = "localhost"
PORT  = 53444
MESSAGES = 1000

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
       # s.sendto(b'hello UDP', (HOST, PORT))
        begin_time = time.time()
        for i in range(MESSAGES):
            s.sendto(b'hello UDP', (HOST, PORT))
        data, addr = s.recvfrom(1024)
        finish_time = time.time()

        rtt = (finish_time - begin_time) * 1000
        print(rtt)

    print(f"{data.decode()}")

if __name__ == "__main__":
    main()