import socket

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 4000))
        line = input(':')
        s.sendall(line.encode())
        resp = s.recv(1024)
        print(f'>{resp.decode()}')


if __name__ == '__main__':
    run()
